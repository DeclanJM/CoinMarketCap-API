import requests
import json
from config import api_key

def get_api_data(max_coin_limit):
    key = api_key

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "X-CMC_PRO_API_KEY": key,
    }

    params = {
        "start": "1",     #Adjust where to start
        "limit": f"{max_coin_limit}",   # Adjust how many coins
        "convert": "USD"  # Adjust the currency
    }

    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    return data