import os
import requests
import asyncio
from telegram import Bot

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def create_analysis():
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": """
برای XAUUSD یک تحلیل کوتاه بده.

فرمت حتما این باشد:

📊 نتیجه:
(روند کلی)

🟢 یا 🔴 نظر:
(خرید یا فروش)

📌 حمایت:
(سطوح مهم)

📌 مقاومت:
(سطوح مهم)

⚠️ ریسک:
(یک خط)

حداکثر ۱۰ خط بنویس.

آخر پیام دقیقا اضافه کن:

@afinace - ai
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

    return result["choices"][0]["message"]["content"]


async def send_analysis():

    if not BOT_TOKEN:
        print("BOT_TOKEN خالی است")
        return

    if not CHAT_ID:
        print("CHAT_ID خالی است")
        return

    analysis = create_analysis()

    bot = Bot(BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
