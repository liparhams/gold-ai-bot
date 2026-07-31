import asyncio

from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID,
    TIMEFRAMES
)

from market import get_market

from chart import create_chart

from analysis import ai_analysis

from news import get_today_news



bot = Bot(
    BOT_TOKEN
)



async def send_bot():



    for name,tf in TIMEFRAMES.items():

        try:


            df = get_market(tf)



            image = create_chart(
                df,
                name
            )



            analysis = ai_analysis(
                df,
                name
            )



            caption = f"""
📊 XAUUSD AI

⏱ تایم فریم: {name}


{analysis}
"""



            # محدودیت تلگرام
            if len(caption) > 900:

                caption = caption[:900]



            with open(
                image,
                "rb"
            ) as photo:


                await bot.send_photo(

                    chat_id=CHAT_ID,

                    photo=photo,

                    caption=caption

                )



        except Exception as e:


            await bot.send_message(

                chat_id=CHAT_ID,

                text=f"""
❌ خطا در {name}

{e}
"""

            )




    # فقط یک پیام اخبار

    news = get_today_news()


    await bot.send_message(

        chat_id=CHAT_ID,

        text=news

    )




if __name__ == "__main__":


    asyncio.run(
        send_bot()
    )
