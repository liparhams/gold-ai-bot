import os
import asyncio
import requests
from telegram import Bot


BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

MODEL = os.environ.get(
    "MODEL",
    "google/gemini-2.0-flash-exp:free"
)


def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + OPENROUTER_API_KEY.strip(),
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Analysis"
    }


    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

یک تحلیل کامل بازار طلا بده.

شرایط:
- فقط تحلیل، نه سیگنال قطعی خرید یا فروش
- تایم فریم 30 دقیقه
- قیمت‌های حمایت و مقاومت باید نزدیک قیمت واقعی فعلی طلا باشند
- اعداد الکی مثل 1600 یا 1900 نده
- تحلیل تکنیکال، روند، ساختار بازار و سناریوها را توضیح بده

فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:

🧱 حمایت‌های مهم:

🚧 مقاومت‌های مهم:

🧠 تحلیل تکنیکال:

🔎 سناریوهای احتمالی:

⚠️ جمع‌بندی:

حداکثر 12 خط.
"""


    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 900,
        "temperature": 0.3
    }


    try:

        r = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )


        result = r.json()


        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return "خطای OpenRouter:\n" + str(result)


    except Exception as e:
        return "خطا:\n" + str(e)



async def send_analysis():

    if not BOT_TOKEN:
        print("BOT_TOKEN خالی است")
        return

    if not CHAT_ID:
        print("CHAT_ID خالی است")
        return


    bot = Bot(
        token=BOT_TOKEN.strip()
    )


    analysis = get_ai_analysis()


    message = f"""
{analysis}


@afinace - ai
"""


    await bot.send_message(
        chat_id=CHAT_ID.strip(),
        text=message
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
