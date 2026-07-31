import asyncio
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID

from market import get_market
from chart import create_chart
from analysis import analyze


bot = Bot(token=BOT_TOKEN)



async def send_analysis():


    timeframes = {

        "30min": "30 دقیقه",

        "4h": "4 ساعته",

        "1day": "روزانه"

    }



    for tf, name in timeframes.items():

        try:


            print(f"Getting {tf} data...")


            data = get_market(tf)


            chart_file = create_chart(
                data,
                tf
            )


            description = str(data[:50])


            text = analyze(
                description
            )


            await bot.send_photo(

                chat_id=CHAT_ID,

                photo=open(
                    chart_file,
                    "rb"
                ),

                caption=f"""

📊 XAUUSD AI ANALYSIS

⏱ تایم فریم:
{name}


{text}


@afinace - ai

"""

            )


            print(
                f"{tf} sent"
            )



        except Exception as e:


            await bot.send_message(

                chat_id=CHAT_ID,

                text=f"""

❌ خطا در تحلیل {tf}

{e}

"""

            )



asyncio.run(
    send_analysis()
)
