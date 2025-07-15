from dagster import Definitions
from .pipeline import shipping_data_product_job
from .schedules import daily_pipeline_schedule

defs = Definitions(
    jobs=[shipping_data_product_job],
    schedules=[daily_pipeline_schedule]
)
