import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY, MODEL


def create_analysis():

    prompt = """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

یک تحلیل تکنیکال کوتاه ولی حرفه‌ای بنویس.

قوانین:
- سیگنال قطعی خرید یا فروش نده.
- قیمت‌های ساختگی تولید نکن.
- اگر داده قیمت یا چارت نداری، واضح بگو.
- حمایت و مقاومت را فقط در صورت داشتن اطلاعات واقعی اعلام کن.
- تحلیل باید حدود 10 تا 15 خط باشد.

فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم:
...

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
        "max_tokens": 700
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    if "choices" not in result:
        return f"خطای OpenRouter: {result}"

    return result["choices"][0]["message"]["content"]


async def send_analysis():

    bot = Bot(BOT_TOKEN)

    analysis = create_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())    bot = Bot(
        token=BOT_TOKEN
    )


    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
