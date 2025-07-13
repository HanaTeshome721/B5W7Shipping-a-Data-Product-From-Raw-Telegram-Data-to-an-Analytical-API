with yolo as (
  select * from raw.yolo_detections
),
messages as (
  select * from {{ ref('fct_messages') }}
)

select
  m.message_id,
  y.detected_class,
  y.confidence,
  y.image_path
from yolo y
join messages m
  on y.channel = m.channel_name
  and y.image_path like concat('%', m.message_id::text, '%')
