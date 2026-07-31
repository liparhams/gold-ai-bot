import requests

from config import (
    OPENROUTER_API_KEY,
    MODEL
)


def analyze(chart_description):


    url="https://openrouter.ai/api/v1/chat/completions"



    headers={

        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type":
        "application/json"

    }



    prompt=f"""

تو تحلیلگر حرفه‌ای XAUUSD هستی.

این داده چارت است:

{chart_description}


تحلیل بده:

📊 XAUUSD

⏱ تایم فریم:

📈 روند:

💰 وضعیت قیمت:

📌 حمایت:

📌 مقاومت:

🧠 تحلیل:

Market Structure
Liquidity
Order Block
BOS
Trend


🔎 سناریو صعود:

🔴 سناریو نزول:

⚠️ جمع بندی:

عدد خیالی نساز.

"""


    body={

        "model":MODEL,

        "messages":[

            {

            "role":"user",

            "content":prompt

            }

        ],

        "max_tokens":2000

    }



    r=requests.post(

        url,

        headers=headers,

        json=body

    )


    result=r.json()


    return result["choices"][0]["message"]["content"]
