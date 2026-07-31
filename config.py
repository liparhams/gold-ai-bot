import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# OpenRouter AI
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Model
MODEL = "meta-llama/llama-3.1-8b-instruct"


# بررسی خطا
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN خالی است")

if not CHAT_ID:
    raise ValueError("CHAT_ID خالی است")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY خالی است")
