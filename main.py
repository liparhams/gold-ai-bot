import requests
import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


def create_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD (Gold) هستی.

هدف فقط تحلیل بازار است، نه دادن سیگنال خرید یا فروش.

یک تحلیل تکنیکال حرفه‌ای و کوتاه ارائه بده.

مواردی که بررسی کن:
- روند کلی بازار
- ساختار قیمت
- تایم فریم چارت
- حمایت و مقاومت مهم
- مناطق عرضه و تقاضا
- Order Block
- Liquidity
- شکست‌ها و واکنش قیمت
- سناریوی احتمالی صعودی و نزولی

فرمت خروجی:

📊 تحلیل XAUUSD

⏱ تایم فریم:
...

📈 وضعیت بازار:
...

📌 حمایت مهم:
...

📌 مقاومت مهم:
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

حداکثر 12 تا 15 خط باشد.
سیگنال مستقیم خرید یا فروش نده.
متن اضافه و کلمات بی‌ربط ننویس.

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
        "temperature": 0.3,
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

    bot = Bot(token=BOT_TOKEN)

    analysis = create_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
