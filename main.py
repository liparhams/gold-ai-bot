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

به زبان فارسی و مناسب کانال تلگرام بنویس.

موارد:
- روند فعلی بازار
- حمایت و مقاومت مهم
- سناریوی خرید
- سناریوی فروش
- مدیریت ریسک

تحلیل کوتاه و کاربردی باشد.
"""


    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
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
