import matplotlib.pyplot as plt
import pandas as pd

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator


def create_chart(df, timeframe):

    df = df.copy()


    # EMA
    df["ema50"] = EMAIndicator(
        close=df["close"],
        window=50
    ).ema_indicator()


    df["ema200"] = EMAIndicator(
        close=df["close"],
        window=200
    ).ema_indicator()


    # RSI
    df["rsi"] = RSIIndicator(
        close=df["close"],
        window=14
    ).rsi()


    plt.figure(
        figsize=(12,6)
    )


    # کندل ساده
    plt.plot(
        df.index,
        df["close"],
        linewidth=1,
        label="XAUUSD"
    )


    plt.plot(
        df.index,
        df["ema50"],
        label="EMA 50"
    )


    plt.plot(
        df.index,
        df["ema200"],
        label="EMA 200"
    )


    plt.title(
        f"XAUUSD {timeframe}"
    )


    plt.xlabel(
        "Time"
    )


    plt.ylabel(
        "Price"
    )


    plt.legend()


    plt.grid()


    file_name = (
        "chart_"
        + timeframe.replace(
            " ",
            "_"
        )
        + ".png"
    )


    plt.tight_layout()


    plt.savefig(
        file_name,
        dpi=200
    )


    plt.close()


    return file_name
