def return_top_coins(api_data):
    s = "Top 100 Cryptocurrencies by Market Cap:\n"

    data = api_data
    i = 0
    for currency in data["data"]:
        name = currency["name"]
        symbol = currency["symbol"]
        price = currency["quote"]["USD"]["price"]
        market_cap = currency["quote"]["USD"]["market_cap"]
        i += 1
        s += f"   {i}:  {name} ({symbol}): ${price:,.2f} | Market Cap: ${market_cap:,.2f}\n"
    return s
