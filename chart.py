import mplfinance as mpf
import pandas as pd


def create_chart(data, timeframe):

    df = pd.DataFrame(data)

    df = df.rename(columns={
        "datetime": "Date",
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close"
    })


    df["Date"] = pd.to_datetime(df["Date"])

    df = df.set_index("Date")

    df = df.astype(float)


    filename = f"XAUUSD_{timeframe}.png"


    ema50 = mpf.make_addplot(
        df["Close"].ewm(span=50).mean()
    )

    ema200 = mpf.make_addplot(
        df["Close"].ewm(span=200).mean()
    )


    mpf.plot(

        df,

        type="candle",

        style="charles",

        addplot=[
            ema50,
            ema200
        ],

        title=f"XAUUSD {timeframe}",

        volume=False,

        savefig=filename

    )


    return filename
