import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY, MODEL


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_ai_analysis():

    prompt = """
تو یک تحلیلگر حرفه‌ای بازار طلا XAUUSD هستی.

هدف: ارائه تحلیل تکنیکال، نه سیگنال خرید یا فروش.

قوانین مهم:
- قیمت لحظه‌ای در اختیار تو نیست.
- هیچ عددی برای قیمت، حمایت یا مقاومت از خودت نساز.
- اگر قیمت واقعی موجود نیست، حمایت و مقاومت را به صورت "ناحیه مهم" توضیح بده.
- از ساختن قیمت‌های قدیمی مثل 1600 یا 2300 خودداری کن.

خروجی دقیقاً با این ساختار:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H

📈 روند بازار:
بررسی روند، سقف‌ها و کف‌ها، قدرت حرکت

💰 وضعیت قیمت:
توضیح وضعیت فعلی بازار بدون عددسازی

📌 حمایت های مهم:
ناحیه‌های احتمالی حمایت و دلیل اهمیت آنها

📌 مقاومت های مهم:
ناحیه‌های احتمالی مقاومت و دلیل اهمیت آنها

🧠 تحلیل تکنیکال:
بررسی:
- Market Structure
- Liquidity
- Order Block
- Break of Structure
- Momentum
- مناطق مهم عرضه و تقاضا

🔎 سناریوها:

🟢 سناریوی صعود:
شرایطی که باعث ادامه حرکت صعودی می‌شود

🔴 سناریوی نزول:
شرایطی که باعث تغییر یا اصلاح نزولی می‌شود

⚠️ جمع بندی:
یک نتیجه حرفه‌ای و کوتاه

در آخر بنویس:

@afinace - ai
"""


    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Afinace AI"
    }


    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1500,
        "temperature": 0.3
    }


    try:

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


    except Exception as e:
        return f"خطای اتصال AI:\n{e}"



async def send_analysis():

    bot = Bot(token=BOT_TOKEN)

    analysis = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )



if __name__ == "__main__":

    asyncio.run(send_analysis())
