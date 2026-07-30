import os

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Market
SYMBOL = "XAUUSD"

TIMEFRAMES = [
    "30m",
    "4h",
    "2d"
]
