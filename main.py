import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
CHANNEL_TO_FORW_ID = int(os.getenv("MAIN_CHANNEL_ID"))

client = TelegramClient("anon", api_id, api_hash)
client.start()

id_array = []
with open("channel_ids.txt") as file:
    id_array = [int(row.strip()) for row in file]


@client.on(events.NewMessage(id_array))
async def main(event):
    await client.forward_messages(CHANNEL_TO_FORW_ID, event.message)


client.run_until_disconnected()
