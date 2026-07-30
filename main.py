import asyncio

from telegram import Bot
from google import genai

from config import (
    TELEGRAM_TOKEN,
    CHANNEL_ID,
    GEMINI_API_KEY
)


client = genai.Client(
    api_key=GEMINI_API_KEY
)


async def create_analysis():

    prompt = """
تحلیل XAUUSD (طلا) انجام بده.

به زبان فارسی بنویس:

1- روند بازار
2- حمایت و مقاومت
3- سناریوی خرید
4- سناریوی فروش
5- مدیریت ریسک

تحلیل کوتاه و مناسب کانال تلگرام باشد.
"""


    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text


async def send_analysis():

    analysis = await create_analysis()

    bot = Bot(
        token=TELEGRAM_TOKEN
    )

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
