import requests

from config import (
    OPENROUTER_API_KEY,
    MODEL
)

from news import get_today_news



def ai_analysis(data, tf):


    prompt = f"""

تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

تایم فریم:
{tf}


داده کندل:

{data}


اخبار مهم امروز:

{get_today_news()}


تحلیل را فقط با این ساختار بده:

📊 XAUUSD AI ANALYSIS

⏱ تایم فریم

📈 Trend

💰 Price

📌 Support

📌 Resistance

🧠 Smart Money

Market Structure:
Liquidity:
Order Block:
BOS:

🟢 سناریو صعود

🔴 سناریو نزول

⚠️ جمع بندی


قوانین:
- عدد خیالی نساز
- سلام و مقدمه ننویس
- تحلیل واقعی بر اساس داده بده
- سیگنال قطعی خرید فروش نده

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

            "max_tokens": 3000,

            "temperature": 0.3,

            "messages":[

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        },

        timeout=90

    )


    result = response.json()


    if "choices" not in result:

        return (
            "❌ خطای OpenRouter:\n"
            + str(result)
        )


    return result["choices"][0]["message"]["content"]
