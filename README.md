# Object-Detection
Object Detection using YOLOv8

This project uses yolov8n.pt from ULTRALYTICS 

## Training 
To train first prepare a dataset

**Preparing Dataset**

Create a '*Dataset*' folder. 

Collect alot of pictures for the object you want to track, ensure pictures covers all angles and have different backgrounds, lighting etc. 

Divide your dataset in a 80-20 split, 80% for training and 20% for validation. Set up directories for training and validation, make sure to use '*train*' and '*val*' for the directory names as YOLOv8 uses these directory names. 

WIthin each directory for training and validation, add directories for images and labels using '*images*' and '*labels*' as directory names

![image](https://github.com/user-attachments/assets/bbe43135-5e8e-4db1-822b-ea1129e0de7a)


![image](https://github.com/user-attachments/assets/ff769afc-3e27-4d70-b462-df59b9408e2a)


Within a conda environment install '*labelimg*' to label your data. 

![image](https://github.com/user-attachments/assets/ef48380d-19c1-42b9-b44c-9695558d3aaa)

Open labelimg and select your '*images*' folder as Open Dir and your '*labels*' folder as Save Dir. 
Make sure you have selected '*YOLO*'

Click '*Create RedBox*' and draw a box around your object, make sure to cover your object properly without any space around the object. Label the box as the name of the object

![image](https://github.com/user-attachments/assets/614c81cf-81f2-42ca-a286-d3b335a0bb2b)

![image](https://github.com/user-attachments/assets/1eff420a-3fcd-4836-8335-cddaf7b0d004)

'*Labelimg*' will save text files within your '*labels*' folder which will store the x,y coordinates and the height and width of your RedBox around each object in each object.

It will create corresponding text files for each image in the '*images*' folder. 

![image](https://github.com/user-attachments/assets/86d23aed-549f-4215-9003-c3adb734836d)


Complete this for both train and val. 

Then in your '*Dataset*' folder create a '*data.yaml*' file. In this file write the directory for your images folder and your labels folder and the label of the object in the following format 

![image](https://github.com/user-attachments/assets/dabf2830-253a-4f51-bb47-1f5e4daea8df)


**Training your model**

Next train your model on your dataset. 

Open Anaconda prompt and activate your environement. (instructions for environment in '*REQUIREMENTS.md*' file)

Run the following command: 

`yolo task=detect mode=train epochs=80 data='Directory to your data.yaml file' model=yolov8n.pt imgsz=640 batch=8`

![image](https://github.com/user-attachments/assets/6f48606d-0442-4605-a23e-415e4ec15ca9)

Once training has elapsed, a '*run*' folder will be automatically created which will store data from the training in a '*train*' folder directory.

1. Confusion Matrix
2. F1 curve
3. Labels correlogram
4. P curve, PR curve and R curve
5. Results xlsx file
6. Batch pictures from the training and the validation


![image](https://github.com/user-attachments/assets/a6385142-0ef1-4909-8733-67ec14212aab)



The confusion matrix shows an overview of the training, it shows when validated on the val dataset, how many were results were from the categories
1. True Positive
2. True Negative
3. False Positive
4. False Negative


![confusion_matrix](https://github.com/user-attachments/assets/37fcc242-2dc4-430d-889f-2a05fa51b392)


## Testing
This project uses real-time testing through use of webcam. 

In the '*runs*' folder, is another folder titled '*Weights*', this stores the best and last models from your training process.

Typically we use the best model. 

For testing the model run the follwoing command in your conda environment:

`yolo task=detect mode=predict model='Your best model name'.pt source=0 conf=0.5 show=True`

![image](https://github.com/user-attachments/assets/c7adc472-3cc9-4264-9b17-1dbe8dbc124b)


![image](https://github.com/user-attachments/assets/8c8dfc85-b690-464f-8b02-03f8661a9f2b)


The model will detect the object and also display a confidence value.
