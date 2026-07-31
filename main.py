import os
import requests
import asyncio
from telegram import Bot


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


if not BOT_TOKEN:
    raise Exception("BOT_TOKEN خالی است")

if not CHAT_ID:
    raise Exception("CHAT_ID خالی است")

if not OPENROUTER_API_KEY:
    raise Exception("OPENROUTER_API_KEY خالی است")


def create_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "max_tokens": 300,
        "messages": [
            {
                "role": "system",
                "content": "تو تحلیلگر XAUUSD هستی. فقط کوتاه و فارسی جواب بده."
            },
            {
                "role": "user",
                "content": """
یک تحلیل کوتاه طلا XAUUSD بده.

قالب دقیقا:

📊 نتیجه:
یک خط درباره روند

🟢 نظر:
خرید یا فروش یا صبر + دلیل کوتاه

📌 حمایت:
سطوح مهم

📌 مقاومت:
سطوح مهم

⚠️ ریسک:
یک خط کوتاه

فقط همین بخش ها.
حداکثر ۱۰ خط.
هیچ متن انگلیسی یا توضیح اضافه ننویس.
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

    if "choices" not in result:
        return "خطای OpenRouter:\n" + str(result)


    text = result["choices"][0]["message"]["content"]

    return text + "\n\n@afinace - ai"



async def send_analysis():

    analysis = create_analysis()

    bot = Bot(BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )



if __name__ == "__main__":
    asyncio.run(send_analysis())
