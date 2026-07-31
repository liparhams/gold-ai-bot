import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


MODEL = "deepseek/deepseek-chat"


def get_ai_analysis():

    api_key = OPENROUTER_API_KEY.strip()

    if not api_key:
        return "❌ OpenRouter API Key خالی است"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Analyzer"
    }

    prompt = """
تو یک تحلیلگر حرفه‌ای بازار طلا هستی.

برای XAUUSD تحلیل تکنیکال بده.

تایم فریم: 4H

خروجی دقیقا با این بخش‌ها باشد:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:

📌 حمایت‌های مهم:
(قیمت‌های واقعی و نزدیک به قیمت فعلی طلا بده)

📌 مقاومت‌های مهم:
(قیمت‌های واقعی و نزدیک به قیمت فعلی طلا بده)

🧠 تحلیل تکنیکال:
(ساختار بازار، روند، نقدینگی، شکست‌ها و مناطق مهم)

🔎 سناریوها:

🟢 سناریوی صعود:
توضیح بده

🔴 سناریوی نزول:
توضیح بده

⚠️ جمع بندی:
خلاصه تحلیل

از دادن عددهای قدیمی و غیرواقعی خودداری کن.
سیگنال خرید یا فروش قطعی نده.
"""

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1800,
        "temperature": 0.4
    }


    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return "❌ خطای OpenRouter:\n" + str(result)

    except Exception as e:
        return "❌ خطای اتصال:\n" + str(e)



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

━━━━━━━━━━━━━━
@afinace - ai
"""


    await bot.send_message(
        chat_id=str(CHAT_ID).strip(),
        text=message
    )



if __name__ == "__main__":
    asyncio.run(send_analysis())
