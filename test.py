import torch
from ultralytics import YOLO

# for object detection in images
model = YOLO("path_to_model(.pt)")  
results = model("path_to_image.jpg")
results[0].show()

# for object detection in video
model = YOLO("path_to_model(.pt)")
results = model.predict(source="path_to_video.mp4", conf=0.75, show=True)