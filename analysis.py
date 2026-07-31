import requests

from config import OPENROUTER_API_KEY, MODEL


def get_analysis(data, timeframe):


    prompt = f"""
تو تحلیلگر حرفه‌ای XAUUSD هستی.

تایم فریم:
{timeframe}

داده کندل:
{data.tail(50).to_string()}


تحلیل فقط با این ساختار:

📈 Trend:
 
💰 Price:

📌 Support:
۳ سطح

📌 Resistance:
۳ سطح

🧠 Smart Money:
Market Structure
Liquidity
Order Block
BOS

🟢 Bullish Scenario:

🔴 Bearish Scenario:

⚠️ Summary:

قوانین:
سلام و مقدمه ننویس.
داستان تعریف نکن.
عدد الکی نساز.
حداکثر 700 کلمه.
"""


    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }


    body = {

        "model": MODEL,

        "messages":[
            {
                "role":"user",
                "content":prompt
            }
        ],

        "max_tokens":1200
    }



    r = requests.post(
        url,
        headers=headers,
        json=body,
        timeout=60
    )


    result = r.json()


    if "choices" not in result:
        raise Exception(result)


    return result["choices"][0]["message"]["content"]
