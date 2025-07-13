select distinct
  sender_id,
  'Lobelia' as channel_name  -- update based on data
from {{ ref('stg_telegram_messages') }}
