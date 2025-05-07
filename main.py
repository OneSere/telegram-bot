from telethon import TelegramClient
import os
from flask import Flask

# Telegram API credentials
api_id = 25843334
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'
session_name = 'anon'  # This will create anon.session

client = TelegramClient(session_name, api_id, api_hash)

# Flask app to bind a port
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

async def main():
    await client.start()
    print("✅ Logged in successfully. Session file 'anon.session' created!")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
    # Running the Flask app, binding it to an open port
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
