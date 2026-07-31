import requests
import pandas as pd


from config import MARKET_API_KEY



def get_market(timeframe):


    url = "https://api.twelvedata.com/time_series"


    params = {

        "symbol":"XAU/USD",

        "interval":timeframe,

        "outputsize":150,

        "apikey":MARKET_API_KEY

    }



    r = requests.get(

        url,

        params=params,

        timeout=30

    )


    data = r.json()



    if "values" not in data:

        raise Exception(
            "داده بازار دریافت نشد"
        )



    df = pd.DataFrame(
        data["values"]
    )



    df = df.rename(

        columns={

            "datetime":"date"

        }

    )



    df["date"] = pd.to_datetime(
        df["date"]
    )



    df = df.set_index(
        "date"
    )



    for c in [

        "open",
        "high",
        "low",
        "close"

    ]:

        df[c] = df[c].astype(float)



    return df.sort_index()
