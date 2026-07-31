import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY, MODEL


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_ai_analysis():

    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

یک تحلیل تکنیکال کامل بده، نه سیگنال خرید و فروش قطعی.

ساختار خروجی:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H

📈 روند بازار:
(صعودی، نزولی یا رنج + توضیح)

💰 وضعیت قیمت:
(بدون ساختن قیمت الکی)

📌 حمایت های مهم:
چند ناحیه مهم بنویس.

📌 مقاومت های مهم:
چند ناحیه مهم بنویس.

🧠 تحلیل تکنیکال:
روند، ساختار بازار، نقدینگی، شکست‌ها و مناطق مهم را توضیح بده.

🔎 سناریوها:

🟢 سناریوی صعود:
توضیح بده چه اتفاقی باعث ادامه رشد می‌شود.

🔴 سناریوی نزول:
توضیح بده چه اتفاقی باعث افت می‌شود.

⚠️ جمع بندی:
یک نتیجه کوتاه تحلیلی بده.

در پایان دقیقاً بنویس:

@afinace - ai
"""


    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Bot"
    }


    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 2000,
        "temperature": 0.4
    }


    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=data,
        timeout=60
    )


    result = response.json()


    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    else:
        return f"خطای OpenRouter:\n{result}"


async def send_analysis():

    bot = Bot(token=BOT_TOKEN)

    text = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
