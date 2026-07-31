import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
CHAT_ID = os.environ.get("CHAT_ID", "").strip()
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "").strip()

MODEL = "openai/gpt-4o-mini"

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN خالی است")

if not CHAT_ID:
    raise Exception("CHAT_ID خالی است")

if not OPENROUTER_API_KEY:
    raise Exception("OPENROUTER_API_KEY خالی است")
