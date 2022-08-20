import requests

bitcoin_api_url = 'https://api.nomics.com/v1/currencies/ticker?key=309e2d11ad8b5499d8c249e384a1c2d6418febd6&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1"'
response = requests.get(bitcoin_api_url)
reponse_json = response.json()  
type(reponse_json)
print(" PRICE",reponse_json[0]['price'],"TIME-STAMP ",reponse_json[0]['price_timestamp'])



# 'https://blockchain.info/ticker'