import os


# Telegram

BOT_TOKEN = os.getenv(
    "BOT_TOKEN"
)

CHAT_ID = os.getenv(
    "CHAT_ID"
)



# AI APIs

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


# اگر بعداً API مستقیم گرفتی اینجا اضافه می‌کنیم

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)


CEREBRAS_API_KEY = os.getenv(
    "CEREBRAS_API_KEY"
)



# Market Data

MARKET_API_KEY = os.getenv(
    "MARKET_API_KEY"
)



# AI Backup order

AI_MODELS = [

    # OpenRouter
    "meta-llama/llama-3.1-8b-instruct",

    "google/gemini-2.0-flash-001",

    "qwen/qwen-2.5-7b-instruct",

    "mistralai/mistral-7b-instruct"

]



# Symbol

SYMBOL = "XAU/USD"



# Timeframes

TIMEFRAMES = {

    "30 دقیقه":
    "30min",

    "4 ساعته":
    "4h",

    "روزانه":
    "1day"

}



# Telegram signature

SIGNATURE = """

@afinace - ai

"""
