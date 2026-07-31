import asyncio

from telegram import Bot

from config import BOT_TOKEN,CHAT_ID

from market import get_market

from chart import create_chart

from analysis import ai_analysis



bot=Bot(
    BOT_TOKEN
)



async def send():


    for tf,name in [

        ("30min","30 دقیقه"),

        ("4h","4 ساعته"),

        ("1day","روزانه")

    ]:


        try:


            data=get_market(tf)



            img=create_chart(
                data,
                tf
            )



            text=ai_analysis(
                data,
                name
            )



            await bot.send_photo(

                CHAT_ID,

                open(img,"rb"),

                caption=
                f"📊 XAUUSD AI\n\n⏱ {name}"

            )



            await bot.send_message(

                CHAT_ID,

                text

            )



        except Exception as e:


            await bot.send_message(

                CHAT_ID,

                f"❌ خطا در {name}\n{e}"

            )



asyncio.run(send())
