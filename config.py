import os

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Channel / Group ID
CHAT_ID = os.getenv("CHAT_ID")


# OpenRouter API
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# AI Model
MODEL = os.getenv(
    "MODEL",
    "google/gemini-2.5-flash"
)


# OpenRouter URL
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
