import requests
import json
from django.shortcuts import render

def home(request):
    # Grab crypto currency price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,XMR&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # Grab crypto news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")  
    api = json.loads(api_request.content)

    # Handle API error or empty data
    if api.get('Response') == 'Error':
        api['Data'] = []

    return render(request, 'home.html', {'api': api, 'price': price})
