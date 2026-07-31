import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, OPENROUTER_API_KEY


def get_ai_analysis():

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + OPENROUTER_API_KEY.strip(),
        "Content-Type": "application/json"
    }

    prompt = """
You are a professional XAUUSD gold market analyst.

Analyze gold price technically.

Rules:
- Do NOT give a direct buy or sell signal.
- Act like an analyst, not a signal bot.
- Create realistic support and resistance zones.
- Explain trend, structure, momentum and scenarios.
- Timeframe: 30M
- Keep it around 10-15 lines.
- Use current gold price context, not old prices.

Format:

📊 تحلیل XAUUSD

⏱ تایم فریم: 30M

📈 روند بازار:

📌 حمایت های مهم:

📌 مقاومت های مهم:

🧠 تحلیل تکنیکال:

🔎 سناریوهای احتمالی:

⚠️ جمع بندی:

@afinace - ai
"""

    data = {
        "model": "google/gemini-2.5-flash",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=90
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    else:
        return "خطای OpenRouter:\n" + str(result)



async def send_analysis():

    bot = Bot(
        token=BOT_TOKEN.strip()
    )

    text = get_ai_analysis()

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


if __name__ == "__main__":
    asyncio.run(send_analysis())
