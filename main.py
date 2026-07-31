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



    for name, interval in TIMEFRAMES.items():


        try:



            df = get_market(
                interval
            )



            image = create_chart(
                df,
                name
            )



            text = ai_analysis(

                df,

                name

            )



            caption = f"""

📊 XAUUSD AI


⏱ تایم فریم:
{name}


{text}

"""



            with open(
                image,
                "rb"
            ) as photo:



                if len(caption) <= MAX_CAPTION:



                    await bot.send_photo(

                        chat_id=CHAT_ID,

                        photo=photo,

                        caption=caption

                    )


                else:



                    await bot.send_photo(

                        chat_id=CHAT_ID,

                        photo=photo,

                        caption=
                        caption[:MAX_CAPTION]

                    )



                    await bot.send_message(

                        chat_id=CHAT_ID,

                        text=
                        "📊 ادامه تحلیل:\n\n"
                        +
                        caption[MAX_CAPTION:4000]

                    )



        except Exception as e:



            await bot.send_message(

                chat_id=CHAT_ID,

                text=
                f"❌ خطا در {name}\n{e}"

            )





    try:



        await bot.send_message(

            chat_id=CHAT_ID,

            text=get_today_news()

        )



    except Exception as e:



        print(e)







if __name__ == "__main__":


    asyncio.run(
        send_bot()
    )
