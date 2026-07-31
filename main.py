import asyncio

from telegram import Bot

from config import BOT_TOKEN, CHAT_ID

from market import get_market
from chart import create_chart
from analysis import analyze



bot = Bot(
    token=BOT_TOKEN
)



async def send_analysis():


    frames = [
        ("30min","30 دقیقه"),
        ("4h","4 ساعته"),
        ("1day","روزانه")
    ]


    for tf, name in frames:

        try:

            print(
                f"Getting {tf}"
            )


            data = get_market(tf)


            chart = create_chart(
                data,
                tf
            )


            analysis = analyze(
                str(data[:100])
            )


            await bot.send_photo(

                chat_id=CHAT_ID,

                photo=open(
                    chart,
                    "rb"
                ),

                caption=f"""
📊 XAUUSD AI ANALYSIS

⏱ تایم فریم:
{name}


{analysis}


@afinace - ai
"""

            )


        except Exception as e:


            print(
                e
            )


            await bot.send_message(

                chat_id=CHAT_ID,

                text=f"""
❌ خطا در {name}

{e}
"""

            )



if __name__ == "__main__":

    asyncio.run(
        send_analysis()
    )
