select
  generate_series::date as date,
  extract(year from generate_series) as year,
  extract(month from generate_series) as month,
  extract(day from generate_series) as day
from generate_series('2024-01-01'::date, current_date, interval '1 day')
