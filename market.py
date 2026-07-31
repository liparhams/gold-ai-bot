import requests
import pandas as pd

from config import MARKET_API_KEY, SYMBOL


def get_market(interval):

    url = "https://api.twelvedata.com/time_series"


    params = {

        "symbol": SYMBOL,

        "interval": interval,

        "outputsize": 150,

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


    df = pd.DataFrame(
        data["values"]
    )


    df["datetime"] = pd.to_datetime(
        df["datetime"]
    )


    df = df.sort_values(
        "datetime"
    )


    for c in [
        "open",
        "high",
        "low",
        "close"
    ]:
        df[c] = pd.to_numeric(
            df[c]
        )


    df = df.set_index(
        "datetime"
    )


    return df
