import ultralytics 
from ultralytics import YOLO

model = YOLO("bottle.pt")  # to load your custom-trained model

source = 0 # for webcam footage

results=model.predict(source, save=True, stream_buffer=True, show=True, conf=0.5,) #args for testing. 