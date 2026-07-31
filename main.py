import asyncio
import requests
from telegram import Bot

# =========================
# تنظیمات
# =========================

BOT_TOKEN = "توکن_ربات_تلگرام_اینجا"
CHAT_ID = "آیدی_کانال_یا_گروه_اینجا"

OPENROUTER_API_KEY = "کلید_OpenRouter_اینجا"


# =========================
# دریافت تحلیل AI
# =========================

def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Bot"
    }

    prompt = """
تو یک تحلیلگر حرفه ای XAUUSD هستی.

تحلیل بده، سیگنال مستقیم نده.

تایم فریم: 4H

قیمت فعلی طلا را در نظر بگیر.

خروجی دقیقا با این بخش ها باشد:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:

📌 حمایت های مهم:
(عددهای واقعی نزدیک قیمت فعلی)

📌 مقاومت های مهم:
(عددهای واقعی نزدیک قیمت فعلی)

🧠 تحلیل تکنیکال:
(حداقل چند خط توضیح)

🔎 سناریوهای احتمالی:

🟢 سناریوی صعودی:

🔴 سناریوی نزولی:

⚠️ جمع بندی:

در آخر فقط این را اضافه کن:

@afinace - ai
"""

    data = {
        "model": "google/gemini-2.0-flash-exp:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1200,
        "temperature": 0.5
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
        return "خطای OpenRouter:\n" + str(result)



# =========================
# ارسال تلگرام
# =========================

async def send_analysis():

    bot = Bot(token=BOT_TOKEN)

    text = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
