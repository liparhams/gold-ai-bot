import os


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv(
    "MODEL",
    "google/gemini-2.5-flash"
)

MARKET_API_KEY = os.getenv("MARKET_API_KEY")


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
