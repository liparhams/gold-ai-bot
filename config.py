import os


BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

OPENROUTER_API_KEY = os.environ.get(
    "OPENROUTER_API_KEY"
)

MARKET_API_KEY = os.environ.get(
    "MARKET_API_KEY"
)


# مدل های پشتیبان
MODELS = [

    "google/gemini-2.0-flash-exp:free",

    "meta-llama/llama-3.1-8b-instruct:free",

    "qwen/qwen-2.5-7b-instruct:free",

    "mistralai/mistral-7b-instruct:free",

    "google/gemma-3-4b-it:free"

]


SYMBOL = "XAU/USD"


TIMEFRAMES = {

    "30 دقیقه": "30min",

    "4 ساعته": "4h",

    "روزانه": "1day"

}


SIGNATURE = "\n\n@afinace - ai"
