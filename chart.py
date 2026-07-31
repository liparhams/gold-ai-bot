import mplfinance as mpf


def create_chart(df, name):

    file = f"{name}.png"


    df2 = df.copy()

    df2.index = df2["time"]


    mpf.plot(
        df2,
        type="candle",
        style="charles",
        title=f"XAUUSD {name}",
        volume=False,
        savefig=file
    )


    return file
