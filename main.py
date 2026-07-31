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



MAX_CAPTION = 1000



async def send_bot():


    for name, tf in TIMEFRAMES.items():

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



            with open(image, "rb") as photo:



                if len(caption) <= MAX_CAPTION:


                    await bot.send_photo(

                        chat_id=CHAT_ID,

                        photo=photo,

                        caption=caption

                    )


                else:


                    first_part = caption[:MAX_CAPTION]


                    second_part = caption[MAX_CAPTION:]


                    await bot.send_photo(

                        chat_id=CHAT_ID,

                        photo=photo,

                        caption=first_part

                    )



                    # ادامه تحلیل

                    await bot.send_message(

                        chat_id=CHAT_ID,

                        text=
                        "📊 ادامه تحلیل:\n\n"
                        +
                        second_part[:3000]

                    )



        except Exception as e:


            await bot.send_message(

                chat_id=CHAT_ID,

                text=
                f"❌ خطا در {name}\n{e}"

            )




    # اخبار فقط یک بار

    try:


        news = get_today_news()


        await bot.send_message(

            chat_id=CHAT_ID,

            text=news[:3000]

        )


    except Exception as e:


        await bot.send_message(

            chat_id=CHAT_ID,

            text=
            f"❌ خطای اخبار\n{e}"

        )





if __name__ == "__main__":


    asyncio.run(
        send_bot()
    )
