import requests

from config import OPENROUTER_API_KEY, AI_MODELS
from news import get_today_news


def ask_ai(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }


    for model in AI_MODELS:

        try:

            r = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content":
                            """
تو تحلیلگر حرفه‌ای XAUUSD هستی.
فقط از داده کندل استفاده کن.
هیچ عددی از خودت نساز.
مقدمه، سلام و توضیح اضافه ننویس.
تحلیل کوتاه و کاربردی بده.
"""
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature":0.1,
                    "max_tokens":1000
                },
                timeout=90
            )


            data=r.json()


            if data.get("choices"):

                return data["choices"][0]["message"]["content"]


        except Exception as e:

            print(
                model,
                e
            )


    return "❌ AI در دسترس نیست."



def ai_analysis(df,timeframe):


    candles=df.tail(80).to_string()


    prompt=f"""

تحلیل XAUUSD

تایم فریم:
{timeframe}


کندل ها:

{candles}


ساختار خروجی:

📊 تحلیل XAUUSD

📈 روند:
(صعودی، نزولی، رنج)

💰 قیمت آخر:

📌 حمایت:
(حداکثر 3 سطح)

📌 مقاومت:
(حداکثر 3 سطح)

🧠 Smart Money:
Market Structure:
Liquidity:
Order Block:
BOS:

🔎 سناریو صعود:

🔴 سناریو نزول:

⚠️ جمع بندی:


قوانین:
- حداکثر 350 کلمه
- قیمت فقط از داده بالا
- اگر مطمئن نیستی بنویس نامشخص
- سیگنال قطعی نده

"""


    return ask_ai(prompt)
