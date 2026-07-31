import matplotlib.pyplot as plt

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator



def create_chart(df, name):

    df = df.copy()


    df["EMA50"] = EMAIndicator(
        df["close"],
        window=50
    ).ema_indicator()


    df["EMA200"] = EMAIndicator(
        df["close"],
        window=200
    ).ema_indicator()


    df["RSI"] = RSIIndicator(
        df["close"],
        window=14
    ).rsi()



    plt.figure(
        figsize=(12,6)
    )


    plt.plot(
        df.index,
        df["close"],
        label="XAUUSD"
    )


    plt.plot(
        df.index,
        df["EMA50"],
        label="EMA50"
    )


    plt.plot(
        df.index,
        df["EMA200"],
        label="EMA200"
    )


    plt.title(
        "XAUUSD " + name
    )


    plt.grid()

    plt.legend()


    file = (
        name
        .replace(" ","_")
        + ".png"
    )


    plt.savefig(
        file,
        dpi=200,
        bbox_inches="tight"
    )


    plt.close()


    return file
