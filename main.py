import asyncio
import os
from datetime import datetime

import pytz

from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID,
    TIMEFRAMES,
    SIGNATURE
)

from market import get_market
from chart import create_chart
from analysis import ai_analysis


bot = Bot(
    token=BOT_TOKEN
)



def market_open():


    tz = pytz.timezone(
        "Europe/London"
    )


    now = datetime.now(tz)


    # شنبه و یکشنبه
    if now.weekday() >= 5:
        return False


    return True




async def send():



    if not market_open():


        await bot.send_message(

            chat_id=CHAT_ID,

            text=
            "⏸ بازار فارکس تعطیل است."

        )


        return



    for title, tf in TIMEFRAMES.items():


        try:


            df = get_market(tf)



            image = create_chart(

                df,

                title

            )



            analysis = ai_analysis(

                df,

                title

            )



            # عکس کوتاه

            await bot.send_photo(

                chat_id=CHAT_ID,

                photo=open(
                    image,
                    "rb"
                ),

                caption=
                f"📊 XAUUSD AI\n\n"
                f"⏱ {title}"

            )



            # متن تحلیل

            await bot.send_message(

                chat_id=CHAT_ID,

                text=
                analysis
                +
                SIGNATURE

            )



        except Exception as e:


            await bot.send_message(

                chat_id=CHAT_ID,

                text=
                f"❌ خطا در {title}\n\n{e}"

            )





if __name__ == "__main__":


    asyncio.run(
        send()
    )
