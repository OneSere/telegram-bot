import os
import asyncio
from telethon import TelegramClient, events
from flask import Flask

# Define your API credentials here
api_id = 25843334
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'
session_name = 'anon'  # Your session file name

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Flask app initialization
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Command handler for "CODE1"
@client.on(events.NewMessage(pattern='CODE1'))
async def handle_code1(event):
    await event.respond('Hello Code 1 responding')
    print("CODE1 received, responded successfully!")

# Start the Telethon client
async def start_telethon():
    await client.start()
    print("Telegram client started and ready to respond!")
    await client.run_until_disconnected()

# Start the Flask app (web server)
def start_flask():
    # Use the environment variable PORT if available, else fallback to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # Set your desired port, 5000 is default for Flask

# Main entry point
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    
    # Run both Flask and Telethon client in parallel
    loop.create_task(start_telethon())  # Start Telethon client
    start_flask()  # Start Flask web server

