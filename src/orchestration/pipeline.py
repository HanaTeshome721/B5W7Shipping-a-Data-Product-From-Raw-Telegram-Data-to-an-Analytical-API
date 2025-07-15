from dagster import op, job
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "src/ingest/telegram_scraper.py"], check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python", "src/db/load_raw.py"], check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "dbt_project"], check=True)
    subprocess.run(["dbt", "test", "--project-dir", "dbt_project"], check=True)

@op
def run_yolo_enrichment():
    subprocess.run(["python", "src/enrich/yolo_detect.py"], check=True)
    subprocess.run(["python", "src/db/load_yolo.py"], check=True)

@job
def shipping_data_product_job():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()
