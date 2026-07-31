import os


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MARKET_API_KEY = os.getenv("MARKET_API_KEY")


MODEL = "google/gemini-2.5-flash"


SYMBOL = "XAU/USD"


TIMEFRAMES = [
    ("30min", "30 دقیقه"),
    ("4h", "4 ساعته"),
    ("1day", "روزانه")
]
