from pydantic import BaseModel

class ProductReport(BaseModel):
    product: str
    count: int

class ChannelActivity(BaseModel):
    channel_name: str
    total_messages: int
    average_per_day: float

class MessageSearchResult(BaseModel):
    message_id: int
    message: str
    channel: str
    date: str
