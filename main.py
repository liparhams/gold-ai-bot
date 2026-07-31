import asyncio
import requests

from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID,
    OPENROUTER_API_KEY,
    MODEL,
    OPENROUTER_URL
)

from market import get_gold_data



def get_ai_analysis():


    market_data = get_gold_data()


    prompt = f"""

تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

داده واقعی بازار:

{market_data}


بر اساس همین داده تحلیل کن.

قوانین:

- سیگنال قطعی خرید یا فروش نده.
- عدد خیالی نساز.
- حمایت و مقاومت را از داده استخراج کن.
- تحلیل کامل بده.


فرمت:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H


📈 روند بازار:


💰 وضعیت قیمت:


📌 حمایت های مهم:


📌 مقاومت های مهم:


🧠 تحلیل تکنیکال:

Market Structure
Liquidity
Order Block
BOS
Trend


🔎 سناریوها:


🟢 سناریوی صعود:


🔴 سناریوی نزول:


⚠️ جمع بندی:


@afinace - ai

"""


    headers = {

        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type":
        "application/json",

        "HTTP-Referer":
        "https://github.com",

        "X-Title":
        "Afinace AI"

    }


    body = {

        "model": MODEL,

        "messages": [

            {

                "role": "user",

                "content": prompt

            }

        ],

        "max_tokens": 2500,

        "temperature": 0.2

    }


    response = requests.post(

        OPENROUTER_URL,

        headers=headers,

        json=body,

        timeout=90

    )


    result = response.json()


    if "choices" in result:

        return result["choices"][0]["message"]["content"]


    return "خطای OpenRouter:\n" + str(result)





async def send_analysis():


    analysis = get_ai_analysis()


    bot = Bot(
        token=BOT_TOKEN
    )


    await bot.send_message(

        chat_id=CHAT_ID,

        text=analysis

    )





if __name__ == "__main__":

    asyncio.run(send_analysis())
