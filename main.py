import asyncio
import requests

from telegram import Bot

from config import (
    TELEGRAM_TOKEN,
    CHANNEL_ID,
    XAI_API_KEY
)


def create_analysis():

    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-3-mini",
        "messages": [
            {
                "role": "user",
                "content": """
تحلیل XAUUSD (طلا) انجام بده.

به زبان فارسی بنویس.

شامل:
- روند فعلی بازار
- حمایت و مقاومت مهم
- سناریوی خرید
- سناریوی فروش
- مدیریت ریسک

تحلیل کوتاه و مناسب کانال تلگرام باشد.
"""
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    print(result)

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    else:
        return "خطای Grok: " + str(result)


async def send_analysis():

    analysis = create_analysis()

    bot = Bot(
        token=TELEGRAM_TOKEN
    )

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
