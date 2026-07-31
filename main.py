import asyncio

from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, TIMEFRAMES

from market import get_market

from analysis import ai_analysis

from chart import create_chart

from news import get_today_news



bot=Bot(
    BOT_TOKEN
)



async def send_analysis():


    for name,tf in TIMEFRAMES.items():


        try:


            df=get_market(tf)


            image=create_chart(
                df,
                name
            )


            text=ai_analysis(
                df,
                name
            )


            caption=f"""
📊 XAUUSD AI

⏱ {name}


{text}
"""


            if len(caption)>950:

                caption=caption[:950]


            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open(image,"rb"),
                caption=caption
            )



        except Exception as e:


            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"❌ خطا در {name}\n{e}"
            )



    # اخبار فقط یک بار

    news=get_today_news()


    await bot.send_message(
        chat_id=CHAT_ID,
        text=news
    )




if __name__=="__main__":

    asyncio.run(
        send_analysis()
    )
