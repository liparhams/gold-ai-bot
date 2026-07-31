import requests
import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


MODEL = "meta-llama/llama-3.1-8b-instruct"


def create_analysis():

    prompt = """
تو یک تحلیلگر حرفه‌ای بازار طلا XAUUSD هستی.

یک تحلیل تکنیکال کوتاه ارائه بده.

قوانین:
- سیگنال قطعی خرید یا فروش نده.
- فقط تحلیل بازار بده.
- حمایت و مقاومت منطقی نزدیک قیمت فعلی طلا باشند.
- عددهای قدیمی مثل 1600 یا 1700 نده.
- خروجی بیشتر از 12 خط نباشد.
- ساختار واضح داشته باشد.

فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H

📈 روند بازار:
...

📌 حمایت:
...

📌 مقاومت:
...

🧠 تحلیل تکنیکال:
...

🔎 سناریوها:
🟢 صعود:
...
🔴 نزول:
...

⚠️ جمع بندی:
...

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
        ],
        "max_tokens": 800,
        "temperature": 0.4
    }


    response = requests.post(
        url,
        headers=headers,
        json=data
    )


    result = response.json()


    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    else:
        return f"خطای OpenRouter:\n{result}"



async def send_analysis():

    if not BOT_TOKEN:
        print("BOT_TOKEN خالی است")
        return

    if not CHAT_ID:
        print("CHAT_ID خالی است")
        return

    analysis = create_analysis()


    bot = Bot(
        token=BOT_TOKEN
    )


    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
