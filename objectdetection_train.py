import ultralytics
from ultralytics import YOLO


model = YOLO("yolov8n.yaml")  # build new model from YAML
model = YOLO("yolov8n.pt")  # load a pretrained model
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

results = model.train(data="c:\Users\Rehan Butt\Desktop\Dataset\data.yaml", epochs=80, imgsz=640)