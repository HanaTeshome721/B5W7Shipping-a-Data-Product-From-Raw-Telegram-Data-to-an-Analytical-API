select
  m.message_id,
  m.sender_id,
  m.date,
  m.has_image,
  c.channel_id,
  d.date_id,
  length(m.message) as message_length
from {{ ref('stg_telegram_messages') }} m
join {{ ref('dim_channels') }} c on m.sender_id = c.sender_id
join {{ ref('dim_dates') }} d on date_trunc('day', m.date) = d.date
