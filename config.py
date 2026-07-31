import os
from dotenv import load_dotenv

# خواندن متغیرهای محیطی
load_dotenv()


# =========================
# Telegram Settings
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# =========================
# OpenRouter Settings
# =========================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# مدل هوش مصنوعی
MODEL = "meta-llama/llama-3.1-8b-instruct"


# =========================
# Check Settings
# =========================

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN خالی است")

if not CHAT_ID:
    raise Exception("CHAT_ID خالی است")

if not OPENROUTER_API_KEY:
    raise Exception("OPENROUTER_API_KEY خالی است")
