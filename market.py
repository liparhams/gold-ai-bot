import requests
from config import MARKET_API_KEY


def get_gold_data():

    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": "XAU/USD",
        "interval": "4h",
        "outputsize": 50,
        "apikey": MARKET_API_KEY
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    data = response.json()

    if "values" not in data:
        return f"خطای دریافت قیمت: {data}"

    candles = data["values"]

    latest = candles[0]

    result = f"""
XAUUSD 4H DATA

Current candle:
Open: {latest['open']}
High: {latest['high']}
Low: {latest['low']}
Close: {latest['close']}

Last candles:
{candles[:10]}
"""

    return result
