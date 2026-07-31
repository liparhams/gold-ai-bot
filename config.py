import os


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")


OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


MARKET_API_KEY = os.getenv(
    "MARKET_API_KEY"
)



SYMBOL = "XAUUSD"



TIMEFRAMES = {

    "30 دقیقه": "30min",

    "4 ساعته": "4h",

    "روزانه": "1day"

}



# اگر یکی قطع شد می‌رود بعدی

AI_MODELS = [

    "meta-llama/llama-3.1-8b-instruct",

    "qwen/qwen-2.5-7b-instruct",

    "mistralai/mistral-7b-instruct"

]
