import requests
from config import MARKET_API_KEY


def get_gold_data():

    if not MARKET_API_KEY:
        return "ERROR: MARKET_API_KEY is empty"


    url = "https://api.twelvedata.com/time_series"


    params = {

        "symbol": "XAU/USD",

        "interval": "4h",

        "outputsize": 50,

        "apikey": MARKET_API_KEY

    }


    try:

        response = requests.get(
            url,
            params=params,
            timeout=30
        )


        data = response.json()


        if "status" in data and data["status"] == "error":

            return (
                "Twelve Data Error:\n"
                + str(data)
            )


        if "values" not in data:

            return (
                "No candle data:\n"
                + str(data)
            )


        candles = data["values"]


        result = """
REAL XAUUSD 4H DATA

"""


        for candle in candles[:20]:

            result += f"""
Open: {candle['open']}
High: {candle['high']}
Low: {candle['low']}
Close: {candle['close']}
----------------
"""


        return result


    except Exception as e:

        return f"Market connection error: {e}"
