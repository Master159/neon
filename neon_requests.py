import requests

#Getting information about the blockchain
response = requests.get("https://beta-devnet-api.neonscan.org/overview/stats")
print(response.json())

#Getting information about the network
response = requests.get("https://beta-devnet-api.neonscan.org/overview/network")
print(response.json())

#Getting information about the last transaction
response = requests.get("https://beta-devnet-api.neonscan.org/transaction/lastest?offset=0&limit=1")
print(response.json())

#Getting information about your transaction
response = requests.get("https://beta-devnet-api.neonscan.org/address/info?address=0xdc8ef00ac6021bb3221621b8b0421bbda8f96ba9")
print(response.json())