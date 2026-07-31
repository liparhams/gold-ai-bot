import requests
import pandas as pd

from config import MARKET_API_KEY, SYMBOL


def get_market(timeframe):

    url = "https://api.twelvedata.com/time_series"


    params = {
        "symbol": SYMBOL,
        "interval": timeframe,
        "outputsize": 200,
        "apikey": MARKET_API_KEY
    }


    response = requests.get(
        url,
        params=params,
        timeout=30
    )


    data = response.json()


    if "values" not in data:
        raise Exception(
            data.get(
                "message",
                str(data)
            )
        )


    df = pd.DataFrame(
        data["values"]
    )


    df["datetime"] = pd.to_datetime(
        df["datetime"]
    )


    df = df.sort_values(
        "datetime"
    )


    for col in [
        "open",
        "high",
        "low",
        "close"
    ]:
        df[col] = pd.to_numeric(
            df[col]
        )


    df = df.set_index(
        "datetime"
    )


    return df
