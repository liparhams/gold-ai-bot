import asyncio

from telegram import Bot

from config import BOT_TOKEN, CHAT_ID

from market import get_market
from chart import create_chart
from analysis import analyze



bot = Bot(
    token=BOT_TOKEN
)



def split_message(text, limit=4000):

    parts = []

    while len(text) > limit:

        index = text[:limit].rfind("\n")

        if index == -1:
            index = limit


        parts.append(
            text[:index]
        )

        text = text[index:]


    if text:
        parts.append(text)


    return parts




async def send_analysis():


    timeframes = [

        ("30min", "30 دقیقه"),

        ("4h", "4 ساعته"),

        ("1day", "روزانه")

    ]



    for tf, name in timeframes:


        try:


            print(
                f"Getting {name}"
            )


            # گرفتن دیتا

            data = get_market(
                tf
            )


            # ساخت عکس چارت

            chart_file = create_chart(

                data,

                tf

            )



            # تحلیل AI

            analysis_text = analyze(

                str(data)

            )



            # ارسال عکس

            await bot.send_photo(

                chat_id=CHAT_ID,

                photo=open(
                    chart_file,
                    "rb"
                ),

                caption=f"""

📊 XAUUSD AI

⏱ تایم فریم:
{name}


@afinace - ai

"""

            )



            # ارسال تحلیل جدا

            messages = split_message(
                analysis_text
            )


            for msg in messages:


                await bot.send_message(

                    chat_id=CHAT_ID,

                    text=f"""

📊 تحلیل XAUUSD

⏱ {name}


{msg}


@afinace - ai

"""

                )



            print(
                f"{name} Done"
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
