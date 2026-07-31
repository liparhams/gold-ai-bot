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



    filename = (
        "charts/"
        + timeframe.replace(" ","_")
        + ".png"
    )



    addplots = [

        mpf.make_addplot(
            data["EMA50"]
        ),


        mpf.make_addplot(
            data["EMA200"]
        )

    ]



    mpf.plot(

        data,

        type="candle",

        style="charles",

        addplot=addplots,

        title=
        f"XAUUSD AI - {timeframe}",

        figsize=(12,6),

        volume=False,

        savefig=filename

    )



    return filename
