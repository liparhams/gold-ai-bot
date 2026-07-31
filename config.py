import os


BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

OPENROUTER_API_KEY = os.environ.get(
    "OPENROUTER_API_KEY"
)

MARKET_API_KEY = os.environ.get(
    "MARKET_API_KEY"
)


MODELS = [
    "qwen/qwen-2.5-7b-instruct:free",
    "google/gemma-3-4b-it:free",
    "mistralai/mistral-7b-instruct:free"
]


SYMBOL = "XAU/USD"


TIMEFRAMES = {
    "30 دقیقه": "30min",
    "4 ساعته": "4h",
    "روزانه": "1day"
}


CANDLE_COUNT = 150


SIGNATURE = "\n\n@afinace - ai"
