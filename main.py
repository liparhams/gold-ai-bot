import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Bot"
    }

    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

برای طلا تحلیل تکنیکال بده.

مهم:
- سیگنال قطعی خرید یا فروش نده.
- عددهای حمایت و مقاومت را منطقی بنویس.
- از قیمت‌های قدیمی استفاده نکن.
- تحلیل را مثل یک تریدر حرفه‌ای توضیح بده.
- فقط 10 تا 12 خط باشد.

فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم: 30M

📈 روند بازار:

📌 حمایت مهم:

📌 مقاومت مهم:

🧠 تحلیل تکنیکال:

🔎 سناریوها:

⚠️ جمع بندی:

@afinace - ai
"""

    data = {
        "model": "google/gemini-2.5-flash",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.4
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=90
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    return "خطای OpenRouter:\n" + str(result)



async def send_analysis():

    bot = Bot(token=BOT_TOKEN)

    analysis = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
