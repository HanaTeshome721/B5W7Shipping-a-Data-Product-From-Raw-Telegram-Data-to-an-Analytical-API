from ultralytics import YOLO
import os, json
from pathlib import Path
import datetime

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # or yolov8s.pt / yolov8m.pt for more accuracy

# Folder to scan
root_dir = Path("data/raw/images")
date_folder = datetime.datetime.now().strftime("%Y-%m-%d")
scan_dir = root_dir / date_folder

results = []

for channel_dir in scan_dir.glob("*"):
    for image_file in channel_dir.glob("*.jpg"):
        detections = model(image_file)
        for d in detections:
            for box in d.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                result = {
                    "image_path": str(image_file),
                    "channel": channel_dir.name,
                    "detected_class": model.names[cls],
                    "confidence": round(conf, 4)
                }
                results.append(result)

# Save detections to JSON for loading
output_path = f"data/raw/yolo_detections/{date_folder}.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"✅ Saved {len(results)} detections to {output_path}")
