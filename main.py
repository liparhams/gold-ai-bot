import asyncio
import requests

from telegram import Bot

from config import (
    TELEGRAM_TOKEN,
    CHANNEL_ID,
    OPENROUTER_API_KEY
)


def create_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": """
یک تحلیل کوتاه XAUUSD (طلا) برای کانال تلگرام بنویس.

شامل:
- روند فعلی بازار
- حمایت و مقاومت
- سناریوی خرید
- سناریوی فروش
- مدیریت ریسک

تحلیل به زبان فارسی و حرفه‌ای باشد.
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
        return "خطای OpenRouter: " + str(result)


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
