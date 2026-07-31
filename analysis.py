import requests

from config import (
    OPENROUTER_API_KEY,
    AI_MODELS
)



def ask_ai(prompt):


    headers = {


        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",


        "Content-Type":
        "application/json"

    }



    for model in AI_MODELS:


        try:


            response = requests.post(


                "https://openrouter.ai/api/v1/chat/completions",


                headers=headers,


                json={


                    "model":model,


                    "messages":[


                        {


                            "role":"system",


                            "content":
                            """
تو تحلیلگر حرفه‌ای XAUUSD هستی.

قوانین:
- فقط از داده کندل استفاده کن
- عدد خیالی نساز
- تحلیل کوتاه و حرفه‌ای باشد
- تکرار نکن
- سیگنال قطعی خرید یا فروش نده
"""

                        },


                        {


                            "role":"user",


                            "content":prompt

                        }


                    ],


                    "temperature":0.1,


                    "max_tokens":1200


                },


                timeout=90

            )



            data=response.json()



            if data.get("choices"):


                return (
                    data["choices"][0]
                    ["message"]
                    ["content"]
                )



        except Exception as e:


            print(
                model,
                e
            )



    return "❌ هیچ مدل AI فعال نیست."







def ai_analysis(df,timeframe):


    candles = (
        df.tail(100)
        .to_string()
    )



    prompt=f"""


تحلیل XAUUSD


تایم فریم:
{timeframe}


داده:

{candles}



ساختار:



📊 تحلیل XAUUSD


📈 روند:


💰 قیمت آخر:


📌 حمایت:
سه سطح مهم


📌 مقاومت:
سه سطح مهم



🧠 Smart Money:


Market Structure:

Liquidity:

Order Block:

BOS:



🔎 سناریو صعود:


🔴 سناریو نزول:


⚠️ جمع بندی:



قوانین:

حداکثر 450 کلمه.
جمله کوتاه.
اگر سطح مشخص نیست بنویس نامشخص.
"""



    return ask_ai(prompt)
