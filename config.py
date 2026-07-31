import os


# Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


# OpenRouter AI
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")


# Market Data
MARKET_API_KEY = os.environ.get("MARKET_API_KEY")


# AI fallback models
MODELS = [
    "qwen/qwen-2.5-7b-instruct:free",
    "google/gemma-3-4b-it:free",
    "mistralai/mistral-7b-instruct:free"
]


# Symbol
SYMBOL = "XAU/USD"


# Timeframes
TIMEFRAMES = {
    "30 دقیقه": "30min",
    "4 ساعته": "4h",
    "روزانه": "1day"
}


# Chart settings
CANDLE_COUNT = 150


# Bot settings
SIGNATURE = "\n\n@afinace - ai"
