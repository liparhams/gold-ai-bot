import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


MODEL = "openai/gpt-4o-mini"


def get_ai_analysis():

    api_key = OPENROUTER_API_KEY.strip()

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Gold AI Bot"
    }


    prompt = """
تو یک تحلیلگر حرفه ای بازار طلا هستی.

برای XAUUSD تحلیل بده.
تایم فریم: 4H

قوانین:
- سیگنال خرید یا فروش نده.
- فقط تحلیل تکنیکال بده.
- حمایت و مقاومت نزدیک قیمت واقعی باشند.
- عددهای قدیمی و اشتباه استفاده نکن.
- توضیحات کوتاه ولی حرفه ای باشد.

فرمت خروجی:

📊 تحلیل XAUUSD

⏱ تایم فریم:
4H

📈 روند بازار:
...

📌 حمایت های مهم:
...

📌 مقاومت های مهم:
...

🧠 تحلیل تکنیکال:
...

🔎 سناریوهای احتمالی:
🟢 سناریوی صعود:
...

🔴 سناریوی نزول:
...

⚠️ جمع بندی:
...

@afinace - ai
"""


    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 2500,
        "temperature": 0.3
    }


    try:

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        result = response.json()


        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        else:
            return "خطای OpenRouter:\n" + str(result)


    except Exception as e:
        return "خطای اتصال:\n" + str(e)



async def send_analysis():

    bot = Bot(
        token=BOT_TOKEN.strip()
    )


    analysis = get_ai_analysis()


    await bot.send_message(
        chat_id=CHAT_ID,
        text=analysis
    )



if __name__ == "__main__":
    asyncio.run(send_analysis())
