import mplfinance as mpf
import pandas as pd


def create_chart(df, name):

    file = f"{name}.png"


    chart = df.copy()


    # تبدیل زمان به تاریخ
    chart["time"] = pd.to_datetime(
        chart["time"]
    )


    # قرار دادن زمان به عنوان index
    chart = chart.set_index(
        "time"
    )


    # مرتب سازی
    chart = chart.sort_index()


    # فقط ستون های لازم
    chart = chart[
        [
            "open",
            "high",
            "low",
            "close"
        ]
    ]


    mpf.plot(
        chart,
        type="candle",
        style="charles",
        title=f"XAUUSD {name}",
        figsize=(12,6),
        volume=False,
        savefig=dict(
            fname=file,
            dpi=150,
            bbox_inches="tight"
        )
    )


    return file
