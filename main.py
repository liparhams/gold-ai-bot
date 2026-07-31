import asyncio
import requests
from telegram import Bot

from config import TELEGRAM_TOKEN, CHANNEL_ID, OPENROUTER_API_KEY


def create_analysis():

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com",
            "X-Title": "Gold AI Bot"
        },
        json={
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": """
تحلیل کوتاه XAUUSD بنویس.
به فارسی.
شامل:
- روند
- حمایت
- مقاومت
- خرید
- فروش
- مدیریت سرمایه
"""
                }
            ]
        },
        timeout=60
    )

    result = response.json()
    print(result)

    if response.status_code == 200:
        return result["choices"][0]["message"]["content"]

    return f"خطای OpenRouter: {result}"


async def send_analysis():
    bot = Bot(token=TELEGRAM_TOKEN)
    text = create_analysis()
    await bot.send_message(chat_id=CHANNEL_ID, text=text)


if __name__ == "__main__":
    asyncio.run(send_analysis())
