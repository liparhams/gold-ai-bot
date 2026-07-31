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
                    "messages":[
                        {
                            "role":"system",
                            "content":
                            "Professional XAUUSD Smart Money analyst. Never invent prices."
                        },
                        {
                            "role":"user",
                            "content":prompt
                        }
                    ],
                    "temperature":0.2,
                    "max_tokens":2500
                },
                timeout=90
            )


            data=r.json()


            if data.get("choices"):

                return data["choices"][0]["message"]["content"]


        except Exception as e:

            print(model,e)


    return "❌ AI unavailable"



def ai_analysis(df,timeframe):


    candles=df.tail(120).to_string()

    news=get_today_news()


    prompt=f"""

Analyze XAUUSD.

Timeframe:
{timeframe}


Candles:
{candles}


News:
{news}


Output:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:

💰 قیمت:

📌 حمایت:

📌 مقاومت:

🧠 Smart Money:
Market Structure:
Liquidity:
Order Block:
BOS:

🔎 سناریو صعود:

🔴 سناریو نزول:

📰 اخبار امروز USD:

⚠️ جمع بندی:


Rules:
- No greetings
- No fake prices
- Use only candle data

"""


    return ask_ai(prompt)
