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


    market = get_gold_data()


    prompt = f"""

تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

این داده واقعی بازار است:

{market}


بر اساس این اطلاعات تحلیل کن.

قوانین:
- سیگنال قطعی خرید یا فروش نده.
- تحلیلگر باش.
- حمایت و مقاومت را از داده بالا استخراج کن.
- عدد خیالی نساز.


فرمت خروجی:

📊 تحلیل XAUUSD


⏱ تایم فریم:
4H


📈 روند بازار:


💰 وضعیت قیمت:


📌 حمایت های مهم:


📌 مقاومت های مهم:


🧠 تحلیل تکنیکال:

بررسی:
Market Structure
Liquidity
Order Block
BOS
Trend


🔎 سناریوها:


🟢 سناریوی صعود:


🔴 سناریوی نزول:


⚠️ جمع بندی:


در آخر:

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

        "max_tokens": 2000,

        "temperature": 0.2

    }



    response = requests.post(

        OPENROUTER_URL,

        headers=headers,

        json=data,

        timeout=90

    )


    result = response.json()



    if "choices" in result:

        return result["choices"][0]["message"]["content"]


    return f"خطای OpenRouter:\n{result}"





async def send_analysis():


    bot = Bot(
        token=BOT_TOKEN
    )


    text = get_ai_analysis()


    await bot.send_message(

        chat_id=CHAT_ID,

        text=text

    )





if __name__ == "__main__":

    asyncio.run(send_analysis())
