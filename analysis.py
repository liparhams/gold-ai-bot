import requests

from config import OPENROUTER_API_KEY, MODEL



def analyze(market_data):


    if not OPENROUTER_API_KEY:

        raise Exception(
            "OPENROUTER_API_KEY موجود نیست"
        )



    url = "https://openrouter.ai/api/v1/chat/completions"



    headers = {

        "Authorization": f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type": "application/json"

    }



    prompt = f"""

تو یک تحلیلگر حرفه‌ای XAUUSD هستی.

داده کندل‌های بازار:

{market_data}


برای طلا تحلیل بده.


قوانین:

- عدد الکی نساز
- فقط بر اساس داده بالا تحلیل کن
- قیمت‌های حمایت و مقاومت را از داده استخراج کن
- سیگنال قطعی خرید یا فروش نده


فرمت خروجی:


📈 روند بازار:

...


💰 وضعیت قیمت:

...


📌 حمایت‌های مهم:

- ...


📌 مقاومت‌های مهم:

- ...


🧠 تحلیل تکنیکال:

Market Structure:
Liquidity:
Order Block:
BOS:
Trend:


🔎 سناریو صعود:

...


🔴 سناریو نزول:

...


⚠️ جمع بندی:

...


حداکثر 1200 توکن جواب بده.
"""



    payload = {

        "model": MODEL,

        "messages": [

            {

                "role": "user",

                "content": prompt

            }

        ],

        "max_tokens": 1200,

        "temperature": 0.3

    }



    response = requests.post(

        url,

        headers=headers,

        json=payload,

        timeout=60

    )



    result = response.json()



    if "choices" not in result:

        raise Exception(
            result
        )



    return result["choices"][0]["message"]["content"]
