import os
import mplfinance as mpf


def create_chart(df, timeframe):

    os.makedirs(
        "charts",
        exist_ok=True
    )


    data = df.copy()


    data["EMA50"] = (
        data["close"]
        .ewm(span=50)
        .mean()
    )


    data["EMA200"] = (
        data["close"]
        .ewm(span=200)
        .mean()
    )



    file = (
        "charts/"
        + timeframe.replace(" ","_")
        + ".png"
    )



    plots = [

        mpf.make_addplot(
            data["EMA50"],
            color="blue"
        ),

        mpf.make_addplot(
            data["EMA200"],
            color="red"
        )

    ]



    mpf.plot(

        data,

        type="candle",

        style="charles",

        addplot=plots,

        title=f"XAUUSD AI {timeframe}",

        volume=False,

        figsize=(12,6),

        savefig=file

    )



    return file
