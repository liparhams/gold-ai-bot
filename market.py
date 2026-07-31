import requests
import pandas as pd

from config import MARKET_API_KEY, SYMBOL


def get_market(interval):

    url = "https://api.twelvedata.com/time_series"


    params = {
        "symbol": SYMBOL,
        "interval": interval,
        "outputsize": 120,
        "apikey": MARKET_API_KEY
    }


    r = requests.get(
        url,
        params=params,
        timeout=30
    )


    data = r.json()


    if "values" not in data:
        raise Exception(data)


    df = pd.DataFrame(data["values"])


    df = df.rename(
        columns={
            "datetime":"time",
            "open":"open",
            "high":"high",
            "low":"low",
            "close":"close"
        }
    )


    for c in ["open","high","low","close"]:
        df[c] = df[c].astype(float)


    df = df.iloc[::-1]


    return df
