import asyncio
import os
from datetime import datetime

from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, TIMEFRAMES
from market import get_market
from analysis import ai_analysis
from chart import create_chart



bot = Bot(
    token=BOT_TOKEN
)



async def send_analysis():


    for name, tf in TIMEFRAMES.items():

        try:

            print(
                "Getting data:",
                name
            )


            df = get_market(tf)


            image_path = create_chart(
                df,
                name
            )


            analysis = ai_analysis(
                df,
                name
            )



            # کپشن عکس کوتاه برای محدودیت تلگرام

            caption_limit = 900


            caption = f"""
📊 XAUUSD AI

⏱ تایم فریم:
{name}

{analysis[:caption_limit]}
"""


            await bot.send_photo(

                chat_id=CHAT_ID,

                photo=open(
                    image_path,
                    "rb"
                ),

                caption=caption

            )



            # ادامه تحلیل اگر طولانی بود

            if len(analysis) > caption_limit:


                for i in range(
                    caption_limit,
                    len(analysis),
                    3500
                ):


                    await bot.send_message(

                        chat_id=CHAT_ID,

                        text=analysis[i:i+3500]

                    )



        except Exception as e:


            await bot.send_message(

                chat_id=CHAT_ID,

                text=f"""
❌ خطا در {name}

{str(e)}
"""

            )





if __name__ == "__main__":


    asyncio.run(
        send_analysis()
    )
