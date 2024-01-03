import requests
import json
from config import api_key

# Replace with your actual CoinMarketCap API key
key = api_key


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    "X-CMC_PRO_API_KEY": key,
}

params = {
    "start": "1",
    "limit": "10",
    "convert": "USD"  # Adjust the currency if needed
}

response = requests.get(url, headers=headers, params=params)
data = json.loads(response.text)

print("Top 10 Cryptocurrencies by Market Cap:\n")

for currency in data["data"]:
    name = currency["name"]
    symbol = currency["symbol"]
    price = currency["quote"]["USD"]["price"]
    market_cap = currency["quote"]["USD"]["market_cap"]

    print(f"\t{name} ({symbol}): ${price:,.2f} | Market Cap: ${market_cap:,.2f}")