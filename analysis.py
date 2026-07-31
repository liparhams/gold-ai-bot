import requests

from config import (
    OPENROUTER_API_KEY,
    MODELS
)

from news import get_today_news



def ask_ai(prompt):

    if not OPENROUTER_API_KEY:

        return "❌ OpenRouter API Key پیدا نشد."


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



    for model in MODELS:


        try:


            print(
                "Trying model:",
                model
            )


            response = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers=headers,

                json={

                    "model": model,

                    "messages":[

                        {

                            "role":
                            "system",

                            "content":
                            "You are a professional XAUUSD forex analyst."

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

                timeout=120

            )


            data = response.json()



            if "choices" in data:


                print(
                    "Working model:",
                    model
                )


                return (
                    data["choices"][0]
                    ["message"]
                    ["content"]
                )



            else:

                print(
                    "Model unavailable:",
                    model,
                    data
                )



        except Exception as e:


            print(
                "Model error:",
                model,
                e
            )



    return """
❌ هیچ مدل AI فعال پیدا نشد.

OpenRouter مدل‌های رایگان را تغییر داده یا محدود کرده است.
"""





def ai_analysis(df, timeframe):


    candles = df.tail(120).to_string()



    news = get_today_news()



    prompt = f"""

تحلیل حرفه‌ای XAUUSD انجام بده.


تایم فریم:
{timeframe}


داده کندل:

{candles}


اخبار مهم امروز USD:

{news}



خروجی فقط با این ساختار:


📊 تحلیل XAUUSD


⏱ تایم فریم:


📈 روند بازار:
(Trend + Market Structure)


💰 وضعیت قیمت:
(قیمت آخر + موقعیت نسبت به ساختار)


📌 حمایت‌های مهم:
(حداقل 3 سطح واقعی از داده)


📌 مقاومت‌های مهم:
(حداقل 3 سطح واقعی از داده)


🧠 Smart Money:

Market Structure:
Liquidity:
Order Block:
BOS:
Trend:


🔎 سناریو صعود:


🔴 سناریو نزول:


📰 اخبار مهم امروز:
(فقط خبرهای مهم قرمز آمریکا)


⚠️ جمع بندی:


قوانین:

- عدد خیالی نساز
- قیمت از داده کندل استخراج شود
- سلام و مقدمه ننویس
- سیگنال قطعی خرید یا فروش نده
- حرفه‌ای و کوتاه ولی کامل بنویس

"""


    return ask_ai(prompt)
