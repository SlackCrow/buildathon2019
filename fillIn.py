from web3 import Web3, HTTPProvider, contract
import json
import time
import csv

infura_url = "https://ropsten.infura.io/v3/806041cdff964ee0b2cbd2ef55cb3122"
wallet_address = "0xE75D9DE667F7FFaCD7a300E02dc4e6654598cA77"
wallet_private_key = "2CE8FABF78D208C16CC4C9A6A379AD83BD8AFAEB52B82CA918B4670D71B9EF42"
count = 1

with open("PropertySaleABI.json") as f:
    info_json1 = json.load(f)
titleAbi = info_json1

with open("PropertyTaxABI.json") as f:
    info_json2 = json.load(f)
taxAbi = info_json2

with open("PropertyMortgageABI.json") as f:
    info_json3 = json.load(f)
mortgageAbi = info_json3

with open("PropertyJudgementABI.json") as f:
    info_json4 = json.load(f)
judgementAbi = info_json4


w3 = Web3(HTTPProvider(infura_url))
w3.eth.enable_unaudited_features()

# 370
contract_address_370_title = "0x401ab1769746945509a9157470a117a89b0da84c"
contract_370_title = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_title), abi = titleAbi)
contract_address_370_tax = "0xd42cc96c18a1e7ff63b26591b2f6810ef41a84bb"
contract_370_tax = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_tax), abi = taxAbi)
contract_address_370_mortgage = "0x72e4b38c27479262f2dc28a1e543fbcf22cae43f"
contract_370_mortgage = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_mortgage), abi = mortgageAbi)
contract_address_370_judgement = "0xb125c5ff745ff9696dc76223daea302369cffa5c"
contract_370_judgement = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_judgement), abi = judgementAbi)

# 170
contract_address_170_title = "0xf546e6d5dfdf47883c6ab4f7321a688663021f24"
contract_170_title = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_title), abi = titleAbi)
contract_address_170_tax = "0x176049f3b85041e1602631ede641e2d1aa4a95a0"
contract_170_tax = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_tax), abi = taxAbi)
contract_address_170_mortgage = "0x43d4a7ab5ea7975a54a5379947ff1f3d48e538a7"
contract_170_mortgage = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_mortgage), abi = mortgageAbi)
contract_address_170_judgement = "0x81fd91107e755c06753c0bc98d2c0307f8884925"
contract_170_judgement = w3.eth.contract(address = Web3.toChecksumAddress(contract_address_370_judgement), abi = judgementAbi)

def proccess_transaction_blockchain(txn_dict):
    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(result)
    count = 0
    while tx_receipt is None and (count < 30):
        time.sleep(20)
        tx_receipt = w3.eth.getTransactionReceipt(result)
        count += 5
        print(tx_receipt)

    if tx_receipt is None:
        print("Transaction failed!")
        return False
    return True

def transact_title(address, buyer, seller, date, price, tranType):
    nonce = w3.eth.getTransactionCount(wallet_address)
    if address == '370':
        txn_dict = contract_370_title.functions.emitSale(address, buyer, seller, date,tranType, price).buildTransaction({
            'chainId': 3,
            'gas': 1500000,
            'gasPrice': w3.toWei(str(40 * count), 'gwei'),
            'nonce': nonce,
        })
    else:
        txn_dict = contract_170_title.functions.emitSale(address, buyer, seller, date,tranType, price).buildTransaction({
            'chainId': 3,
            'gas': 1500000,
            'gasPrice': w3.toWei(str(40 * count), 'gwei'),
            'nonce': nonce,
        })
    proccess_transaction_blockchain(txn_dict)

def transact_tax(address, owner, taxYear, taxesRecieved):
    nonce = w3.eth.getTransactionCount(wallet_address)
    if address == '370':
        txn_dict = contract_370_title.functions.emitTax(address, owner, taxYear, taxesRecieved).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    else:
        txn_dict = contract_170_title.functions.emitTax(address, owner, taxYear, taxesRecieved).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    proccess_transaction_blockchain(txn_dict)

def transact_mortgage(address, owner, amount, balance, status):
    nonce = w3.eth.getTransactionCount(wallet_address)
    if address == '370':
        txn_dict = contract_370_title.functions.emitMortgage(address, owner, amount, balance,status).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    else:
        txn_dict = contract_170_title.functions.emitMortgage(address, owner, amount, balance,status).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    proccess_transaction_blockchain(txn_dict)

def transact_judgement(address, owner, casenumber, description, filedate, amount):
    nonce = w3.eth.getTransactionCount(wallet_address)
    if address == '370':
        txn_dict = contract_370_title.functions.emitJudgement(address, owner, casenumber, description,filedate,amount).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    else:
        txn_dict = contract_170_title.functions.emitJudgement(address, owner, casenumber, description,filedate,amount).buildTransaction({
            'chainId': 3,
            'gas': 1400000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })
    proccess_transaction_blockchain(txn_dict)

def parsePrice(input):
    toParse = ''
    for word in input:
        if word.isdigit():
            toParse = toParse + word
    if toParse == '':
        toParse = '0'
    return int(toParse)
