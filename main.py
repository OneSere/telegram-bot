from telethon import TelegramClient, events
import asyncio
import schedule
import time
import threading

# === Your Telegram API credentials ===
api_id = 25843334
api_hash = 'e752bb9ebc151b7e36741d7ead8e4fd0'
session_name = 'anon'  # Keep the generated .session file

# === Initialize the Telegram client ===
client = TelegramClient(session_name, api_id, api_hash)

# === Respond to incoming messages ===
@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text.lower()
    if "code1" in text:
        await event.respond("Hello Code 1 responding.")
    elif "hi" in text:
        await event.respond("I'm currently away. Will get back to you soon!")

# === Repeating message to specific user ===
async def send_repeated_message():
    user = '@gostaddy'
    for _ in range(5):
        try:
            await client.send_message(user, 'hi how are you?')
            await asyncio.sleep(5)
        except Exception as e:
            print("Error sending message:", e)

# === Scheduler in separate thread ===
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# === Main entry point ===
async def main():
    schedule.every(1).seconds.do(lambda: asyncio.ensure_future(send_repeated_message()))

    # Start scheduler in background
    threading.Thread(target=run_schedule, daemon=True).start()

    # Start the Telegram client
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

# === Run everything ===
if __name__ == "__main__":
    asyncio.run(main())
