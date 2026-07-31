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


    try:

        r = requests.get(
            url,
            params=params,
            timeout=30
        )


        data = r.json()


        if "values" not in data:
            return f"Market API Error: {data}"


        candles = data["values"]


        text = "XAUUSD 4H candles:\n\n"


        for c in candles[:10]:

            text += (
                f"Open: {c['open']} "
                f"High: {c['high']} "
                f"Low: {c['low']} "
                f"Close: {c['close']}\n"
            )


        return text


    except Exception as e:

        return f"Market connection error: {e}"
