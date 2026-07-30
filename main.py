import telebot
import google.generativeai as genai

from config import (
    TELEGRAM_TOKEN,
    CHANNEL_ID,
    GEMINI_API_KEY
)


# Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)


# Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def create_analysis():

    prompt = """
    تحلیل XAUUSD (طلا) انجام بده.

    تحلیل شامل:
    - روند فعلی بازار
    - حمایت و مقاومت
    - سناریوی خرید
    - سناریوی فروش
    - مدیریت ریسک

    تحلیل را به زبان فارسی و مناسب انتشار در کانال تلگرام بنویس.
    """

    response = model.generate_content(prompt)

    return response.text


def send_analysis():

    analysis = create_analysis()

    bot.send_message(
        CHANNEL_ID,
        analysis
    )


if __name__ == "__main__":
    send_analysis()
