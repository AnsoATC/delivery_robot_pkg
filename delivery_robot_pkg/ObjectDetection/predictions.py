from ultralytics import YOLO

# Load a model
#model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('./models/traffic_signs_weight.pt')  # load a custom model
#model = YOLO('./model/best.pt').load('yolov8n.pt')  # build from YAML and transfer weights

##Predict Method Takes all the parameters of the Command Line Interface

#model.predict(source="0", show=True, conf=0.15, save=True)
model.predict(source="./ressources/Screenshot2.png", show=True, conf=0.15, save=True)