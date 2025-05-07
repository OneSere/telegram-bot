from telethon import TelegramClient, events
import os
from flask import Flask
import asyncio
import time

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

# Away message and response to CODE1
away_message = "I'm currently away. I will respond as soon as I'm available."
@client.on(events.NewMessage(pattern='CODE1'))
async def handler(event):
    await event.respond('Hello Code 1 responding')
    print("Received CODE1")

# Away message handler
@client.on(events.NewMessage(pattern='/away'))
async def away_handler(event):
    await event.respond(away_message)
    print("Responded with away message")

# Scheduled message system
async def scheduled_message():
    while True:
        # Send a message to @gostaddy every 5 seconds for 5 times
        for i in range(5):
            try:
                user = await client.get_entity('@gostaddy')
                await client.send_message(user, 'Hii, how are you?')
                print(f"Sent message {i+1}")
            except Exception as e:
                print(f"Error sending message: {e}")
            await asyncio.sleep(5)  # wait for 5 seconds between each message
        await asyncio.sleep(60)  # wait for 1 minute before sending again

async def main():
    await client.start()
    print("✅ Logged in successfully. Session file 'anon.session' created!")
    
    # Start the scheduled message in the background
    client.loop.create_task(scheduled_message())

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
    
    # Running the Flask app, binding it to an open port
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
