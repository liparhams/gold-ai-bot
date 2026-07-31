import pandas as pd
import mplfinance as mpf


def create_chart(data,name):


    df=pd.DataFrame(data)


    df["time"]=pd.to_datetime(
        df["time"]
    )


    df=df.set_index(
        "time"
    )


    df=df.sort_index()



    df["EMA50"]=df["close"].ewm(
        span=50
    ).mean()



    df["EMA200"]=df["close"].ewm(
        span=200
    ).mean()



    file=f"{name}.png"



    mpf.plot(

        df,

        type="candle",

        style="charles",

        addplot=[

            mpf.make_addplot(
                df["EMA50"]
            ),

            mpf.make_addplot(
                df["EMA200"]
            )

        ],

        figsize=(12,6),

        savefig=file

    )



    return file
