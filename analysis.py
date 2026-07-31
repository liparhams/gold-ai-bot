import requests

from config import OPENROUTER_API_KEY
from news import get_today_news



AI_MODELS = [

    "meta-llama/llama-3.1-8b-instruct",

    "google/gemini-2.0-flash-001",

    "qwen/qwen-2.5-7b-instruct",

    "mistralai/mistral-7b-instruct"

]



def ask_ai(prompt):


    if not OPENROUTER_API_KEY:

        return "❌ کلید OpenRouter وجود ندارد."



    headers = {

        "Authorization":
        f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type":
        "application/json",

        "HTTP-Referer":
        "https://github.com",

        "X-Title":
        "Gold AI Bot"

    }



    for model in AI_MODELS:


        try:


            print(
                "Trying AI:",
                model
            )


            response = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers=headers,

                json={

                    "model":
                    model,


                    "messages":[

                        {

                            "role":
                            "system",

                            "content":
                            """
تو یک تحلیلگر حرفه‌ای فارکس هستی.
فقط بر اساس داده واقعی تحلیل کن.
عدد خیالی نساز.
"""

                        },

                        {

                            "role":
                            "user",

                            "content":
                            prompt

                        }

                    ],


                    "temperature":
                    0.2,


                    "max_tokens":
                    4000

                },


                timeout=90

            )



            data = response.json()



            if data.get("choices"):


                print(
                    "AI OK:",
                    model
                )


                return (

                    data["choices"][0]
                    ["message"]
                    ["content"]

                )



            else:


                print(
                    "AI failed:",
                    model,
                    data
                )



        except Exception as e:


            print(
                "AI error:",
                model,
                e
            )



    return """
❌ هیچ موتور AI پاسخ نداد.
"""






def ai_analysis(df, timeframe):


    candles = df.tail(120).to_string()


    news = get_today_news()



    prompt = f"""

تحلیل XAUUSD انجام بده.


تایم فریم:

{timeframe}



داده کندل:

{candles}



اخبار اقتصادی امروز:

{news}



خروجی:


📊 تحلیل XAUUSD


⏱ تایم فریم:


📈 روند بازار:

(Trend + Market Structure)


💰 وضعیت قیمت:

(آخرین قیمت و شرایط)


📌 حمایت‌های مهم:

حداقل ۳ سطح واقعی


📌 مقاومت‌های مهم:

حداقل ۳ سطح واقعی


🧠 Smart Money:


Market Structure:

Liquidity:

Order Block:

BOS:

Trend:



🔎 سناریو صعود:


🔴 سناریو نزول:


📰 اخبار مهم USD امروز:


⚠️ جمع بندی:



قوانین:

- مقدمه و سلام ننویس
- فقط تحلیل بده
- قیمت ساختگی نساز
- سیگنال قطعی خرید فروش نده

"""


    return ask_ai(prompt)
