import requests

from config import (
OPENROUTER_API_KEY,
MODEL
)

from news import get_today_news



def ai_analysis(data,tf):


    prompt=f"""

تو تحلیلگر حرفه ای XAUUSD هستی.

تایم فریم:
{tf}


داده کندل:

{data}



اخبار امروز آمریکا:

{get_today_news()}



فقط تحلیل بده.

بدون سلام.
بدون مقدمه.

شامل:

Trend

Price

Support

Resistance

Market Structure

Liquidity

Order Block

BOS

سناریو صعود

سناریو نزول

جمع بندی



عدد خیالی نساز.

"""



    r=requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={

        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type":
        "application/json"

        },


        json={

        "model":MODEL,

        "max_tokens":2500,

        "messages":[

            {

            "role":"user",

            "content":prompt

            }

        ]

        }

    )



    result=r.json()


    return result["choices"][0]["message"]["content"]
