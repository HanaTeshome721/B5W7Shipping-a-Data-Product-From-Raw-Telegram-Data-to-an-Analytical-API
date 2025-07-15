from fastapi import FastAPI
from crud import get_top_products, get_channel_activity, search_messages

app = FastAPI()

@app.get("/api/reports/top-products")
def top_products(limit: int = 10):
    return get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity")
def channel_activity(channel_name: str):
    return get_channel_activity(channel_name)

@app.get("/api/search/messages")
def search(query: str):
    return search_messages(query)
