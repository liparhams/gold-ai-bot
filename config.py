import os

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Google Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Market
SYMBOL = "XAUUSD"
TIMEFRAMES = [
    "30m",
    "4h",
    "2d"
]
