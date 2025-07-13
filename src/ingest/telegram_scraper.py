from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os, json, datetime, base64

load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
channels = ["https://t.me/lobelia4cosmetics", "https://t.me/tikvahpharma"]

client = TelegramClient('anon', api_id, api_hash)

# Helper function to recursively make data JSON serializable
def make_json_serializable(obj):
    if isinstance(obj, dict):
        return {k: make_json_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [make_json_serializable(item) for item in obj]
    elif isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, bytes):
        return base64.b64encode(obj).decode('utf-8')  # safely encode bytes
    else:
        return obj

async def scrape_channel(channel):
    messages = []
    async for msg in client.iter_messages(channel, limit=100):
        msg_dict = msg.to_dict()
        msg_clean = make_json_serializable(msg_dict)
        messages.append(msg_clean)

    date_folder = datetime.datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"data/raw/telegram_messages/{date_folder}", exist_ok=True)

    filename = f"data/raw/telegram_messages/{date_folder}/{channel.split('/')[-1]}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    print(f"✅ Scraped {len(messages)} messages from {channel}")

async def main():
    async with client:
        for ch in channels:
            try:
                await scrape_channel(ch)
            except Exception as e:
                print(f"❌ Error scraping {ch}: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
