from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "6141105459:AAG2QgssXPV2at540w1CextAZJIrSRH8Kq4")

API_ID = int(os.environ.get("API_ID", "3566507"))

API_HASH = os.environ.get("API_HASH", "194e4ba8b6787e11274f47ae63eb56ba")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
