import torch
from ultralytics import YOLO


model = YOLO("yolo11n.pt")
model.train(
    data="kvasir.yaml",
    epochs=50,
    batch=5,
    imgsz=640,
)