import os
from telethon import TelegramClient, events
from flask import Flask
import asyncio

# Telegram API credentials
api_id = 25843334  # Your API ID here
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'  # Your API Hash here
session_name = 'anon'  # Name of the session file (anon.session will be created)

client = TelegramClient(session_name, api_id, api_hash)

# Flask app (necessary for platforms like Render/Vercel)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Away message handler
away_message = "I'm currently away. I will respond as soon as I'm available."

@client.on(events.NewMessage(pattern='CODE1'))
async def handler(event):
    """ Handle the 'CODE1' command. """
    await event.respond('Hello Code 1 responding')
    print("Received CODE1 and responded")

@client.on(events.NewMessage(pattern='/away'))
async def away_handler(event):
    """ Handle the '/away' command. """
    await event.respond(away_message)
    print("Responded with away message")

# Start Telethon client and Flask server
async def start_bot():
    await client.start()
    print("✅ Logged in successfully. Session file 'anon.session' created!")
    await client.run_until_disconnected()

# Start Flask server (binding to open port)
def start_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Run both Flask and Telethon in parallel
    loop.create_task(start_bot())  # Telethon bot
    start_flask()  # Flask web server

