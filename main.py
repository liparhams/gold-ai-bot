import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


MODEL = "openai/gpt-4o-mini"


def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Bot"
    }

    prompt = """
تو یک تحلیلگر حرفه ای طلا هستی.

برای XAUUSD تحلیل تکنیکال بده.
تایم فریم: 4H

خروجی فقط با این ساختار باشد:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:
(صعودی، نزولی یا رنج + دلیل کوتاه)

📌 حمایت های مهم:
(سطوح واقعی و نزدیک قیمت فعلی)

📌 مقاومت های مهم:
(سطوح واقعی و نزدیک قیمت فعلی)

🧠 تحلیل تکنیکال:
(ساختار بازار، روند، نقدینگی، شکست ها)

🔎 سناریوها:
🟢 سناریوی صعود:
🔴 سناریوی نزول:

⚠️ جمع بندی:
(خلاصه تحلیل)

در آخر دقیقا این را اضافه کن:

@afinace - ai
"""


    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 3000,
        "temperature": 0.4
    }


    response = requests.post(
        url,
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
