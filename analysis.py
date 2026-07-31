import requests

from config import (
    OPENROUTER_API_KEY,
    MODEL
)

from news import get_today_news



def ai_analysis(data, tf):


    prompt = f"""
تو تحلیلگر حرفه‌ای XAUUSD هستی.

تایم فریم:
{tf}

داده کندل:
{data}

اخبار مهم امروز آمریکا:
{get_today_news()}


تحلیل بده شامل:

📈 Trend
💰 Price
📌 Support
📌 Resistance
🧠 Market Structure
💧 Liquidity
📦 Order Block
🔹 BOS
🟢 سناریو صعود
🔴 سناریو نزول
⚠️ جمع بندی


قانون:
عدد خیالی نساز.
مقدمه و سلام نده.
"""



    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={

            "Authorization":
            f"Bearer {OPENROUTER_API_KEY}",

            "Content-Type":
            "application/json"

        },

        json={

            "model": MODEL,

            "max_tokens": 2500,

            "messages":[

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        },

        timeout=60

    )


    result = response.json()



    # اگر OpenRouter خطا داد

    if "choices" not in result:

        return (
            "❌ خطای OpenRouter:\n\n"
            + str(result)
        )



    return result["choices"][0]["message"]["content"]
