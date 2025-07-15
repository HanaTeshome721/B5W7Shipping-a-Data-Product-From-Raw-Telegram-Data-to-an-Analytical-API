initalized the main repo 🚢 B5W7: Shipping a Data Product – From Raw Telegram Data to an Analytical API

An end-to-end data pipeline that scrapes public Telegram channels, enriches images with YOLOv8 object detection, transforms data using dbt, and exposes insights through a FastAPI-powered analytical API. The entire pipeline is orchestrated and scheduled using Dagster.

---

## 📦 Project Structure

B5W7Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API/
├── data/
│ └── raw/ # Raw data lake (messages, images, YOLO detections)
├── dbt_project/ # dbt transformations (models, tests, docs)
├── src/
│ ├── ingest/ # Telegram scraping scripts
│ │ └── telegram_scraper.py
│ ├── db/ # Raw loader scripts
│ │ ├── load_raw.py
│ │ └── load_yolo.py
│ ├── enrich/ # YOLO object detection
│ │ └── yolo_detect.py
│ ├── api/ # FastAPI app
│ │ ├── main.py
│ │ ├── crud.py
│ │ ├── schemas.py
│ │ ├── models.py
│ │ └── database.py
│ └── orchestration/ # Dagster jobs & scheduling
│ ├── pipeline.py
│ ├── schedules.py
│ └── repository.py
├── .env # API keys & DB secrets (excluded from version control)
├── requirements.txt
├── Dockerfile (optional)
├── docker-compose.yml (optional)
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/B5W7Shipping-a-Data-Product.git
cd B5W7Shipping-a-Data-Product
2. Create a .env File
env
Copy code
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
3. Create Virtual Environment and Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
4. Setup PostgreSQL
Create the following schemas and tables:

sql
Copy code
CREATE SCHEMA raw;

CREATE TABLE raw.telegram_messages (
    message_id BIGINT PRIMARY KEY,
    message TEXT,
    sender_id BIGINT,
    date TIMESTAMP,
    has_media BOOLEAN
);

CREATE TABLE raw.yolo_detections (
    message_id BIGINT,
    detected_class TEXT,
    confidence FLOAT,
    image_path TEXT,
    channel TEXT
);
🚀 Running the Pipeline
Step 1: Scrape Telegram Messages
bash
Copy code
python src/ingest/telegram_scraper.py
Step 2: Load Raw Data to PostgreSQL
bash
Copy code
python src/db/load_raw.py
Step 3: Run YOLO Object Detection
bash
Copy code
python src/enrich/yolo_detect.py
python src/db/load_yolo.py
Step 4: Run dbt Transformations
bash
Copy code
cd dbt_project
dbt run
dbt test
Step 5: Launch FastAPI API
bash
Copy code
uvicorn src.api.main:app --reload
Step 6: Launch Dagster UI
bash
Copy code
dagster dev -f src/orchestration/repository.py
📊 API Endpoints
Endpoint	Description
GET /api/reports/top-products?limit=10	Top mentioned products
GET /api/channels/{channel_name}/activity	Daily posting volume for a channel
GET /api/search/messages?query=paracetamol	Search for messages by keyword

🛠 Tools Used
Tool	Purpose
Telethon	Telegram scraping
dbt	Data transformation & modeling
YOLOv8 (Ultralytics)	Object detection in images
FastAPI	Analytical API
Dagster	Orchestration and scheduling
PostgreSQL	Data warehouse backend

📈 Data Model (Star Schema)
dim_channels: Metadata about each Telegram channel

dim_dates: Calendar/time dimension

fct_messages: Core fact table for messages

fct_image_detections: Object detection results linked to messages

🧪 Testing
dbt not_null and unique tests on primary keys

Custom tests: e.g., no messages with null dates

Dagster logs and retries on failure

🧠 Business Questions Answered
What are the most frequently mentioned medical products?

Which channels have the most media (images)?

What is the daily/weekly activity for each channel?

What objects (e.g., pills, bottles) are most common in medical images?

📅 Scheduling
The full pipeline is scheduled to run daily using Dagster schedules

View and configure in the Dagster UI (http://localhost:3000)

📄 License
MIT License © 2025 Kara Solutions

👥 Contributors
Your Name – Data Engineer

Kara Solutions Team – Instruction & Review

yaml
Copy code

---

Let me know if you'd like:
- A PDF version of this README
- Docker instructions added
- GitHub badges for deployment, docs, or tests






Ask ChatGPT



Tools


