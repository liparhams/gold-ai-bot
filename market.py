import requests
from config import MARKET_API_KEY


def get_market(timeframe):

    if not MARKET_API_KEY:
        raise Exception(
            "❌ MARKET_API_KEY در Secret یا config وجود ندارد"
        )


    url = "https://api.twelvedata.com/time_series"


    params = {

        "symbol": "XAU/USD",

        "interval": timeframe,

        "outputsize": 200,

        "apikey": MARKET_API_KEY

    }


    try:

        response = requests.get(
            url,
            params=params,
            timeout=30
        )


        data = response.json()



        if "values" not in data:

            raise Exception(
                f"Twelve Data Error: {data}"
            )



        candles = []


        for item in reversed(data["values"]):

            candles.append({

                "datetime": item["datetime"],

                "open": float(item["open"]),

                "high": float(item["high"]),

                "low": float(item["low"]),

                "close": float(item["close"])

            })



        return candles



    except requests.exceptions.RequestException as e:

        raise Exception(
            f"خطای اتصال به Market API: {e}"
        )
