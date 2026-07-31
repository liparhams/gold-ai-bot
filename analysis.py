import requests
from config import OPENROUTER_API_KEY
from news import get_today_news



def get_available_models():

    try:

        r = requests.get(

            "https://openrouter.ai/api/v1/models",

            headers={
                "Authorization":
                f"Bearer {OPENROUTER_API_KEY}"
            },

            timeout=30

        )


        data = r.json()


        models = []


        for m in data.get("data", []):

            name = m.get("id")


            if name:

                models.append(name)



        return models[:30]


    except Exception:

        return []





def ask_ai(prompt):


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



    backup_models = [

        "meta-llama/llama-3.1-8b-instruct",

        "google/gemini-2.0-flash-001",

        "qwen/qwen-2.5-7b-instruct",

        "mistralai/mistral-7b-instruct"

    ]



    # مدل های جدید OpenRouter

    live_models = get_available_models()



    models = backup_models + live_models



    checked = set()



    for model in models:


        if model in checked:

            continue


        checked.add(model)



        try:


            print(
                "Trying:",
                model
            )



            r = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers=headers,

                json={

                    "model": model,

                    "messages":[

                        {

                            "role":
                            "system",

                            "content":
                            "You are expert XAUUSD forex analyst."

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



            data = r.json()



            if "choices" in data:


                print(
                    "SUCCESS:",
                    model
                )


                return (
                    data["choices"][0]
                    ["message"]
                    ["content"]
                )



        except Exception as e:


            print(
                "FAILED:",
                model,
                e
            )



    return (
        "❌ تمام موتورهای AI "
        "در دسترس نیستند."
    )






def ai_analysis(df, timeframe):


    candles = df.tail(120).to_string()


    news = get_today_news()



    prompt = f"""

تحلیل حرفه‌ای XAUUSD بده.


تایم فریم:
{timeframe}


کندل‌ها:

{candles}


اخبار امروز:

{news}



قالب:

📊 تحلیل XAUUSD

⏱ تایم فریم:

📈 روند بازار:

💰 قیمت:

📌 حمایت‌ها:

📌 مقاومت‌ها:


🧠 Smart Money:

Market Structure:
Liquidity:
Order Block:
BOS:
Trend:


🔎 سناریو صعود:


🔴 سناریو نزول:


📰 اخبار مهم USD:


⚠️ جمع بندی:


قوانین:

- عدد خیالی نساز
- فقط از داده استفاده کن
- سیگنال قطعی نده
- مقدمه ننویس

"""


    return ask_ai(prompt)
