import requests
import time
from datetime import datetime

# # Add key in the key parameter in url before running the script

ethereum_api_url = 'https://api.nomics.com/v1/currencies/ticker?key=&ids=ETH,BTC&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
ifttt_webhook_url = "https://maker.ifttt.com/trigger/dev_test/json/with/key/bnyuBAEItT2GFAHslUQwi2"

def get_ethereum_price():
     response = requests.get(ethereum_api_url)
     reponse_json = response.json()  
     notifier_ifttt= requests.post(ifttt_webhook_url)
     return float(reponse_json[0]['price'])
     

def post_notification(event, value):
    data = {'value1': value}
    ifttt_event_url =  ifttt_webhook_url.format(event)
    requests.post(ifttt_event_url, json=data)

def main():
    pass

if __name__ == '__main__':
    main()










