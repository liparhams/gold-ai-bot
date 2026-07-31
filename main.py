import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY, MODEL


def get_ai_analysis():

    prompt = """
تو یک تحلیلگر حرفه‌ای بازار طلا XAUUSD هستی.

یک تحلیل تکنیکال واقعی و کوتاه بده.

قوانین:
- سیگنال خرید یا فروش قطعی نده.
- حمایت و مقاومت را با عددهای منطقی نزدیک قیمت فعلی بنویس.
- عددهای قدیمی و غیرواقعی نساز.
- ساختار بازار، روند، حمایت، مقاومت و سناریو را توضیح بده.
- خروجی فقط 10 خط باشد.

فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند:

📌 حمایت:

📌 مقاومت:

🧠 تحلیل:

🔎 سناریو:

⚠️ جمع بندی:

@afinace - ai
"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
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

    return "خطا در دریافت تحلیل:\n" + str(result)


async def send_analysis():

    bot = Bot(token=BOT_TOKEN)

    text = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
