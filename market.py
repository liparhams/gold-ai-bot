import requests
from config import MARKET_API_KEY


def get_market(interval):


    url = "https://api.twelvedata.com/time_series"


    params = {

        "symbol":"XAU/USD",

        "interval":interval,

        "outputsize":100,

        "apikey":MARKET_API_KEY

    }


    r=requests.get(
        url,
        params=params
    )


    data=r.json()


    if "values" not in data:

        raise Exception(data)



    candles=[]


    for x in data["values"]:

        candles.append({

            "time":x["datetime"],

            "open":float(x["open"]),

            "high":float(x["high"]),

            "low":float(x["low"]),

            "close":float(x["close"])

        })


    return candles
