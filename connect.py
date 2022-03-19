import requests
import json
from decouple import config

#Authenticate and get accessToken
url = "https://testidentity.quantoznexus.com/connect/token"
params = {
        "client_id": config("CLIENT_ID"), 
        "client_secret": config("CLIENT_SECRET"),
        "scope": config("SCOPE"),
        "grant_type": config("GRANT_TYPE")
        }
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
x = requests.post(url, data=params, headers=headers)
accessToken = json.loads(x.content)["access_token"]

"""
#Check EUR currency
url = "https://testapi.quantoznexus.com/prices/eur"
headers = {"api_version": "1.2", "Authorization": "Bearer " + accessToken}
y = requests.get(url, headers=headers)
print(json.loads(y.content))

#Check currency reserves
url = "https://testapi.quantoznexus.com/reserves"
headers = {"api_version": "1.2", "Authorization": "Bearer " + accessToken}
z = requests.get(url, headers=headers)
print(json.loads(z.content))


#Create new account
# Create XLM account keypair here: https://accountviewer.stellar.org/
customerCode = 5
body = {
    "accountType": "Token",
    "cryptoCode": "XLM",
    "customerCryptoAddress": "GBFCWBDVSE2DBXRLCJFVDH5OGKUJ7MEWHLT3EFZTL2LA5C2I5ZMIM2FB", #generated a new XLM wallet as a test
    "custodianSettings": {
        "generateReceiveAddress": True
    }
}
headers = {"api_version": "1.2", "Authorization": "Bearer " + accessToken}
url = "https://testapi.quantoznexus.com/customer/"+str(customerCode)+"/accounts"
z = requests.post(url, headers=headers, json=body)
print(json.loads(z.content))

"""
#Check customer number
customerNumber = 5
url = "https://testapi.quantoznexus.com/customer/"+str(customerNumber)
headers = {"api_version": "1.2", "Authorization": "Bearer " + accessToken}
a = requests.get(url, headers=headers)
print(json.loads(a.content))


"""
#Create customer
headers = {"api_version": "1.2", "Authorization": "Bearer " + accessToken}
body = {
    "customerCode": "5",
    "trustLevel": "Trusted",
    "currencyCode": "EUR",
    "email": "testcustomer@student.hu.nl",
    "countryCode": "NL",
    "isBusiness": False
}
url = "https://testapi.quantoznexus.com/customer"
b = requests.post(url, headers=headers, json=body)
print(json.loads(b.content))
"""