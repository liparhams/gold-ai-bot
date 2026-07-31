import requests
from config import MARKET_API_KEY



def get_market(timeframe):


    url="https://api.twelvedata.com/time_series"


    params={

        "symbol":"XAU/USD",

        "interval":timeframe,

        "outputsize":100,

        "apikey":MARKET_API_KEY

    }


    r=requests.get(
        url,
        params=params,
        timeout=30
    )


    data=r.json()


    if "values" not in data:

        raise Exception(data)


    return data["values"]
