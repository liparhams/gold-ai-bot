import os


BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHAT_ID = os.environ.get("CHAT_ID")

OPENROUTER_API_KEY = os.environ.get(
    "OPENROUTER_API_KEY"
)

MARKET_API_KEY = os.environ.get(
    "MARKET_API_KEY"
)


MODEL = "google/gemini-2.0-flash-exp:free"


# چک امنیتی
required = {
    "BOT_TOKEN": BOT_TOKEN,
    "CHAT_ID": CHAT_ID,
    "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
    "MARKET_API_KEY": MARKET_API_KEY
}


for key,value in required.items():

    if not value:
        raise Exception(
            f"Missing secret: {key}"
        )
