import asyncio

from telegram import Bot


from config import (
    BOT_TOKEN,
    CHAT_ID,
    TIMEFRAMES
)


from market import get_market
from chart import create_chart
from analysis import get_analysis



bot = Bot(
    token=BOT_TOKEN
)



async def send_analysis():


    for interval, name in TIMEFRAMES:


        try:

            print("Getting", name)


            df = get_market(interval)


            image = create_chart(
                df,
                interval
            )


            text = get_analysis(
                df,
                name
            )


            caption = (
                f"📊 XAUUSD AI\n\n"
                f"⏱ تایم فریم: {name}\n\n"
                + text
            )


            if len(caption) > 1000:

                caption = caption[:950] + "\n\n..."



            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open(image,"rb"),
                caption=caption
            )



        except Exception as e:


            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"❌ خطا در {name}\n\n{e}"
            )



if __name__ == "__main__":

    asyncio.run(
        send_analysis()
    )
