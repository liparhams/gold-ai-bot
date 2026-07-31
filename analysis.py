import requests
import pandas as pd

from config import OPENROUTER_API_KEY, MODELS
from news import get_today_news


def ask_ai(prompt):

    for model in MODELS:

        try:

            r = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers={
                    "Authorization":
                    f"Bearer {OPENROUTER_API_KEY}",

                    "Content-Type":
                    "application/json"
                },


                json={

                    "model": model,

                    "max_tokens": 3500,

                    "temperature": 0.2,

                    "messages":[

                        {
                            "role":"user",
                            "content":prompt
                        }

                    ]

                },

                timeout=90
            )


            data = r.json()


            if "choices" in data:

                return data["choices"][0]["message"]["content"]


        except Exception:

            continue


    return "❌ هیچ مدل AI در دسترس نیست."




def ai_analysis(df, timeframe):


    last = df.tail(100).to_string()


    news = get_today_news()


    prompt = f"""

تو تحلیلگر حرفه‌ای XAUUSD هستی.

تایم فریم:
{timeframe}


داده کندل:

{last}


اخبار امروز:

{news}


یک تحلیل حرفه‌ای بده:


📊 XAUUSD AI ANALYSIS


⏱ تایم فریم:


📈 Trend:
روند با ساختار بازار


💰 Price:
قیمت فعلی


📌 Support:
سه حمایت مهم


📌 Resistance:
سه مقاومت مهم


🧠 Smart Money:


Market Structure:
Liquidity:
Order Block:
BOS:
Trend:


🔎 سناریو صعود:


🔴 سناریو نزول:


⚠️ جمع بندی:


قوانین:

- مقدمه ننویس
- سلام ننویس
- عدد از خودت نساز
- سیگنال قطعی نده
- فقط بر اساس داده کندل تحلیل کن

"""


    return ask_ai(prompt)
