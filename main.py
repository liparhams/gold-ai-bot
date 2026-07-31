import os
import requests
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def create_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = """
برای طلا XAUUSD یک تحلیل کوتاه بده.

فرمت دقیقا:

📊 نتیجه:
(حداکثر 2 خط)

🟢 حمایت:
(سطوح مهم)

🔴 مقاومت:
(سطوح مهم)

📈 نظر معامله:
(خرید یا فروش یا صبر)

⚠️ ریسک:
(یک خط)

حداکثر 10 خط بنویس.
از توضیحات اضافه خودداری کن.
"""

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 300
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    if "choices" not in result:
        return f"خطای OpenRouter: {result}"

    text = result["choices"][0]["message"]["content"]

    return text + "\n\n@afinace - ai"


async def send_analysis():

    bot = Bot(token=TELEGRAM_TOKEN)

    analysis = create_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
