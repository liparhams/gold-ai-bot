import requests

from config import OPENROUTER_API_KEY, AI_MODELS



def ask_ai(prompt):


    headers = {

        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type":
        "application/json"

    }



    for model in AI_MODELS:


        try:


            print(
                "Trying:",
                model
            )


            r = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers=headers,

                json={

                    "model":model,

                    "messages":[

                        {

                            "role":"system",

                            "content":
                            """
تو یک تحلیلگر حرفه‌ای XAUUSD هستی.
فقط از داده کندل استفاده کن.
عدد خیالی نساز.
سلام و مقدمه ننویس.
تحلیل کوتاه و کاربردی بده.
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


            data = r.json()



            if data.get("choices"):


                return (
                    data["choices"][0]
                    ["message"]
                    ["content"]
                )



            print(
                "Model failed:",
                model,
                data
            )



        except Exception as e:

            print(
                model,
                e
            )



    return "❌ هیچ مدل AI فعال نیست."





def ai_analysis(df,timeframe):


    candles = df.tail(80).to_string()



    prompt=f"""

تحلیل XAUUSD

تایم فریم:
{timeframe}


داده کندل:

{candles}



ساختار خروجی:

📊 تحلیل XAUUSD

📈 روند:

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
- فقط قیمت‌های داخل داده
- اگر چیزی مشخص نیست بگو نامشخص
- سیگنال قطعی نده

"""


    return ask_ai(prompt)
