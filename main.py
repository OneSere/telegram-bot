import logging
import asyncio
from telethon import TelegramClient, events

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

# Your fixed Telegram API credentials
api_id = 25843334
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'

# Initialize Telethon client
client = TelegramClient('session_name', api_id, api_hash)

# Flag to activate away message
away_message_enabled = True
away_response_text = "I'm currently away. Will get back to you soon."

# Event handler for new messages
@client.on(events.NewMessage)
async def handler(event):
    message = event.message.text.strip()
    print(f"New message received: {message}")

    # Respond to CODE1
    if message.upper() == "CODE1":
        await event.reply("Hello Code 1 responding")
        print("Replied to CODE1")

    # Away message response
    elif away_message_enabled:
        await event.reply(away_response_text)
        print("Sent away message")

# Scheduled message function
async def scheduled_message():
    for i in range(5):  # Repeat 5 times
        try:
            await client.send_message('@gostaddy', 'hii how are you ?')
            print(f"Sent scheduled message {i+1}/5")
        except Exception as e:
            print(f"Error sending message: {e}")
        await asyncio.sleep(5)  # Wait 5 seconds before next send

# Main function
async def main():
    await client.start(phone='+918829960217')
    print("Bot is running...")

    # Start the scheduled message task
    asyncio.create_task(scheduled_message())

    # Keep the client running
    await client.run_until_disconnected()

# Run the client
client.loop.run_until_complete(main())
