import requests
import time
from datetime import datetime

# # Add key in the key parameter in url before running the script
ethereum_api_url = 'https://api.nomics.com/v1/currencies/ticker?key=309e2d11ad8b5499d8c249e384a1c2d6418febd6&ids=ETH,BTC&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
ifttt_webhook_url = "https://maker.ifttt.com/trigger/{}/json/with/key/bnyuBAEItT2GFAHslUQwi2"

def get_ethereum_price():
     response = requests.get(ethereum_api_url)
     reponse_json = response.json()  
     notifier_ifttt= requests.post(ifttt_webhook_url)
     return float(reponse_json[0]['price'])
     

def post_notification(event, value):
    print('check event',event , value)
    data = {'value1': value}
    ifttt_event_url =  ifttt_webhook_url.format(event)
    requests.post(ifttt_event_url, json=data)



def format_telegram(ethereum_history):
    rows = []
    for ethereum_price in ethereum_history:
        date = ethereum_price['date'].strftime('%d.%m.%Y %H:%M')
        price = ethereum_price['price']

        row = "{}: $<b>{}</b>".format(date, price)
        rows.append(row)
        return '<br>'.join(rows)

    

def main():
    ethereum_history = []
    priceThreshold = 2000
   
    while True:
        price = get_ethereum_price()
        date = datetime.now()
        ethereum_history.append({"date" : date ,"price" : price})

        #emergency notification 
        if price < priceThreshold:
            post_notification('crypto_price_emergency' , price)

        
        
        #daily price alert telegram 
        if len(ethereum_history) == 5:
            post_notification('ethereum_price_update' , format_telegram(ethereum_history))

            ethereum_history = []

        time.sleep(1*5)


if __name__ == '__main__':
    print('main function')
    main()










