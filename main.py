import asyncio
import requests

from telegram import Bot
from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

یک تحلیل کوتاه ولی حرفه‌ای بده.
سیگنال قطعی خرید یا فروش نده.
اعداد حمایت و مقاومت الکی نساز.

ساختار خروجی دقیقاً:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H

📈 روند بازار:
(صعودی، نزولی یا رنج + دلیل)

📌 حمایت‌های مهم:
(فقط اگر مطمئن هستی)

📌 مقاومت‌های مهم:
(فقط اگر مطمئن هستی)

🧠 تحلیل تکنیکال:
روند، ساختار قیمت، نقدینگی، مناطق مهم

🔎 سناریوها:

🟢 سناریوی صعودی:
توضیح کوتاه

🔴 سناریوی نزولی:
توضیح کوتاه

⚠️ جمع‌بندی:
چند خط نتیجه تحلیل

در آخر فقط بنویس:

@afinace - ai
"""

    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 700
    }


    response = requests.post(
        url,
        headers=headers,
        json=data
    )


    result = response.json()


    if "choices" not in result:
        return "خطای OpenRouter:\n" + str(result)


    return result["choices"][0]["message"]["content"]



async def send_analysis():

    if not BOT_TOKEN:
        print("BOT_TOKEN خالی است")
        return

    if not CHAT_ID:
        print("CHAT_ID خالی است")
        return

    bot = Bot(BOT_TOKEN)

    text = get_ai_analysis()


    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
