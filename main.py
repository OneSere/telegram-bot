from telethon import TelegramClient, events
import os
from flask import Flask
import asyncio

# Your Telegram API credentials
api_id = 25843334  # Your API ID here
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'  # Your API Hash here
session_name = 'anon'  # Name of the session file (anon.session will be created)

client = TelegramClient(session_name, api_id, api_hash)

# Flask app to create an open port for deployment platforms (Render, Vercel, etc.)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Away message
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

# Scheduled message system: send message to @gostaddy every 5 seconds for 5 times
async def scheduled_message():
    while True:
        # Send message 5 times to @gostaddy with 5 seconds interval
        for i in range(5):
            try:
                user = await client.get_entity('@gostaddy')  # Replace @gostaddy with the correct username
                await client.send_message(user, 'Hii, how are you?')
                print(f"Sent message {i + 1}")
            except Exception as e:
                print(f"Error sending message: {e}")
            await asyncio.sleep(5)  # wait for 5 seconds before sending the next message
        await asyncio.sleep(60)  # wait 1 minute before repeating the 5 messages

# Main function to handle client connection and background tasks
async def main():
    await client.start()
    print("✅ Logged in successfully. Session file 'anon.session' created!")
    
    # Start the scheduled messages task
    client.loop.create_task(scheduled_message())

if __name__ == "__main__":
    # Run the client and the Flask web server in parallel
    with client:
        client.loop.run_until_complete(main())
    
    # Run the Flask web server (binds to open port)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
