import os


# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# OpenRouter AI
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# مدل Vision برای دیدن چارت
MODEL = "google/gemini-2.5-flash"


# Market Data API
MARKET_API_KEY = os.getenv("MARKET_API_KEY")


# Symbol
SYMBOL = "XAU/USD"


# Timeframes
TIMEFRAMES = [
    "30min",
    "4h",
    "1day"
]


# تعداد کندل برای تحلیل
OUTPUT_SIZE = 120


# بررسی Secret ها
def check_config():

    missing = []

    keys = {
        "BOT_TOKEN": BOT_TOKEN,
        "CHAT_ID": CHAT_ID,
        "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
        "MARKET_API_KEY": MARKET_API_KEY
    }


    for name, value in keys.items():

        if not value:
            missing.append(name)


    if missing:
        raise Exception(
            "Missing Secrets: " + ", ".join(missing)
        )
