import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


MODEL = "google/gemini-2.0-flash-exp:free"


MARKET_API_KEY = os.getenv(
    "MARKET_API_KEY"
)
