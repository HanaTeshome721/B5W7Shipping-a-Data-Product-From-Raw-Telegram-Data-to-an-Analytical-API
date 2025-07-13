with raw as (
  select * from raw.telegram_messages
)

select
  id as message_id,
  sender_id,
  message,
  date::timestamp,
  case when has_media then true else false end as has_image
from raw
