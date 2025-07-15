from dagster import ScheduleDefinition
from .pipeline import shipping_data_product_job

daily_pipeline_schedule = ScheduleDefinition(
    job=shipping_data_product_job,
    cron_schedule="0 6 * * *",  # Every day at 6 AM
    name="daily_shipping_schedule"
)
