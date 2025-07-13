import os, json, psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost",  # <- change this
    port="5432"
)


def load_raw_json_to_db():
    root = "data/raw/telegram_messages"
    for date_folder in os.listdir(root):
        path = os.path.join(root, date_folder)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                data = json.load(f)

            with conn.cursor() as cur:
                for msg in data:
                    cur.execute("""
                        INSERT INTO raw.telegram_messages (message_id, message, sender_id, date, has_media)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING;
                    """, (
                        msg.get('id'), msg.get('message'), msg.get('sender_id'),
                        msg.get('date'), bool(msg.get('media'))
                    ))
            conn.commit()

if __name__ == "__main__":
    load_raw_json_to_db()
