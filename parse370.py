import csv
import datetime
import dateutil
import json
from dateutil import parser

transactions = []

def parsePrice(input):
    toParse = ''
    for word in input:
        if word.isdigit():
            toParse = toParse + word
    if toParse == '':
        toParse = '0'
    return int(toParse)

def processDate(input):
    toProcess = ''
    wasComma = False
    for word in input:
        if not wasComma:
            toProcess = toProcess + word
            if word == ',':
                wasComma = True
        else:
            if word == ' ':
                wasComma = False
                toProcess = toProcess + word
            else:
                wasComma = False
                toProcess = toProcess + ' ' + word

def processBoolean(input):
    if input == 'Y':
        return True
    elif input == 'F':
        return False
        
with open('370-title-data.csv', mode='r', encoding = "ISO-8859-1") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        transactionToAdd = {}
        rowDict = dict(row)
        transactionToAdd['seller'] = rowDict['Seller']
        transactionToAdd['buyer'] = rowDict['Buyer']
        transactionToAdd['date'] = rowDict['Date']
        transactionToAdd['tax'] = []
        transactionToAdd['mortgage'] = []
        transactionToAdd['judgement'] = []
        transactionToAdd['transactionType'] = rowDict['Transaction Type']
        transactionToAdd['price'] = parsePrice(rowDict['Price '])
        transactions.append(transactionToAdd)

with open('370-tax-data.csv', mode='r', encoding = "ISO-8859-1") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        rowDict = dict(row)
        for transaction in transactions:
            if transaction['seller'] == rowDict['Owner']:
                taxToAdd = {}
                taxToAdd['amount'] = parsePrice(rowDict['Amount'])
                taxToAdd['year'] = rowDict['Tax year']
                taxToAdd['paid'] = processBoolean(rowDict['Taxes Received'])
                transaction['tax'].append(taxToAdd)

with open('370-tax-data.csv', mode='r', encoding = "ISO-8859-1") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        rowDict = dict(row)
        for transaction in transactions:
            if transaction['seller'] == rowDict['Owner']:
                taxToAdd = {}
                taxToAdd['amount'] = parsePrice(rowDict['Amount'])
                taxToAdd['year'] = rowDict['Tax year']
                taxToAdd['paid'] = processBoolean(rowDict['Taxes Received'])
                transaction['tax'].append(taxToAdd)

with open('370-morgage-data.csv', mode='r', encoding = "ISO-8859-1") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        rowDict = dict(row)
        for transaction in transactions:
            if transaction['seller'] == rowDict['Owner']:
                taxToAdd = {}
                taxToAdd['amount'] = parsePrice(rowDict['Mortgage Amount'])
                taxToAdd['balance'] = parsePrice(rowDict['Current Balance'])
                transaction['mortgage'].append(taxToAdd)

with open('370-judgement-data.csv', mode='r', encoding = "ISO-8859-1") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        rowDict = dict(row)
        for transaction in transactions:
            if transaction['seller'] == rowDict['Owner']:
                taxToAdd = {}
                taxToAdd['caseNum'] = int(rowDict['Case Number'])
                taxToAdd['description'] = rowDict['Judgement Description']
                taxToAdd['date'] = rowDict['Judgement File Date']
                taxToAdd['amount'] = parsePrice(rowDict['Amount'])
                transaction['judgement'].append(taxToAdd)


with open('result370.json', 'w') as fp:
    json.dump(transactions, fp)
