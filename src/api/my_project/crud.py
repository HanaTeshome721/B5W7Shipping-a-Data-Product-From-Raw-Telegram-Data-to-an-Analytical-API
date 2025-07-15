from database import conn
from schemas import ProductReport, ChannelActivity, MessageSearchResult

def get_top_products(limit: int):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT product, COUNT(*) as count
            FROM fct_messages
            WHERE product IS NOT NULL
            GROUP BY product
            ORDER BY count DESC
            LIMIT %s
        """, (limit,))
        rows = cur.fetchall()
    return [ProductReport(product=r[0], count=r[1]) for r in rows]


def get_channel_activity(channel_name: str):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT channel_name, COUNT(*), COUNT(*) / COUNT(DISTINCT DATE(date))::float
            FROM fct_messages
            WHERE channel_name = %s
            GROUP BY channel_name
        """, (channel_name,))
        row = cur.fetchone()
    if row:
        return ChannelActivity(channel_name=row[0], total_messages=row[1], average_per_day=row[2])
    return {"detail": "Channel not found"}


def search_messages(query: str):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT message_id, message, channel_name, date
            FROM fct_messages
            WHERE message ILIKE %s
            LIMIT 20
        """, (f"%{query}%",))
        rows = cur.fetchall()
    return [MessageSearchResult(message_id=r[0], message=r[1], channel=r[2], date=str(r[3])) for r in rows]
