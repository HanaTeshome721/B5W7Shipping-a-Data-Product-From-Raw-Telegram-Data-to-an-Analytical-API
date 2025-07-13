import json, os, psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port="5432"
)

def load_yolo_detections():
    folder = "data/raw/yolo_detections"
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            data = json.load(f)

        with conn.cursor() as cur:
            for row in data:
                cur.execute("""
                    INSERT INTO raw.yolo_detections (image_path, channel, detected_class, confidence)
                    VALUES (%s, %s, %s, %s)
                """, (
                    row['image_path'], row['channel'], row['detected_class'], row['confidence']
                ))
        conn.commit()

if __name__ == "__main__":
    load_yolo_detections()
