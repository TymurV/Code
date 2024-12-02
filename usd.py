import requests
import time
API_KEY = 'Your API key'
URL = f'http://api.currencylayer.com/live?access_key={API_KEY}&currencies=UAH&source=USD&format=1'

def check_currency():
    response = requests.get(URL)
    data = response.json()
    
    if data['success']:
        usd_to_uah = data['quotes']['USDUAH']
        print(f'1 dollar at this point in time is: {usd_to_uah} UAH')
    else:
        print('Error while receiving data on exchange rate.')

    time.sleep(10)
    check_currency()
check_currency()