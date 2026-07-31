import os
import matplotlib.pyplot as plt
import mplfinance as mpf


def create_chart(df, timeframe):

    try:

        os.makedirs(
            "charts",
            exist_ok=True
        )


        data = df.copy()


        # EMA بدون کتابخانه ta
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


        filename = (
            "charts/"
            + timeframe.replace(" ","_")
            + ".png"
        )


        addplots = [

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

            addplot=addplots,

            title=f"XAUUSD AI - {timeframe}",

            volume=False,

            savefig=filename

        )


        return filename



    except Exception as e:

        print(
            "Chart error:",
            e
        )

        raise e
