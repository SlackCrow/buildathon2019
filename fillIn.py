from web3 import Web3, HTTPProvider, contract
import json

infura_url = "https://ropsten.infura.io/v3/806041cdff964ee0b2cbd2ef55cb3122"
wallet_address = "0xE75D9DE667F7FFaCD7a300E02dc4e6654598cA77"
wallet_private_key = "2CE8FABF78D208C16CC4C9A6A379AD83BD8AFAEB52B82CA918B4670D71B9EF42"

with open("abi.json") as f:
    info_json = json.load(f)
abi = info_json

w3 = Web3(HTTPProvider(infura_url))
w3.eth.enable_unaudited_features()

# 370
contract_address_370_title = "0x5413e651436fa60c4270f9f535b150cfeb471578"
contract_370_title = w3.eth.contract(address = contract_address_370_title, abi = abi)
contract_address_370_tax = "0xa29a0098624149359af7099013ef9fae6c5cb961"
contract_370_tax = w3.eth.contract(address = contract_address_370_tax, abi = abi)
contract_address_370_mortgage = "0x12d310e5ced09fde82269e02991c4176c0c2bcc5"
contract_370_mortgage = w3.eth.contract(address = contract_address_370_mortgage, abi = abi)
contract_address_370_judgement = "0x882616bd12e3d54ad6f99b42aa868bf45e90f472"
contract_370_judgement = w3.eth.contract(address = contract_address_370_judgement, abi = abi)

# 170
contract_address_170_title = "0x9d54e3b53a923958a6310996e9072010b667c60c"
contract_170_title = w3.eth.contract(address = contract_address_370_title, abi = abi)
contract_address_170_tax = "0xbfe9d624a4fc9fe272d1786ef9ab602db6561541"
contract_170_tax = w3.eth.contract(address = contract_address_370_tax, abi = abi)
contract_address_170_mortgage = "0x14aa7df6a9aecdbc9f2803433d81927110ae1367"
contract_170_mortgage = w3.eth.contract(address = contract_address_370_mortgage, abi = abi)
contract_address_170_judgement = "0x71d5bc88eb43a532ff8964b337aeeac14b78db12"
contract_170_judgement = w3.eth.contract(address = contract_address_370_judgement, abi = abi)
