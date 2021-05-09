# Object Detection Webapp

Deploying an Object Detection Service.  
    
This is a simple web-app that detects objects in images. Users can upload their image files and run the object detection to identify objects that on the image.  

## Installation

```
pip install -r requirements.txt  
python app.py
```

## How to Use
1. Upload an image file with objects you'd like to detect
2. Your image should appear in the space below
3. Click the "Start Detection" button to start detecting!
4. The objects that are detected will be bounded by boxes.

## List of Detectable Objects

List of objects classes can be found [here](https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv).  
Information about the dataset the detector is trained on can be found [here](https://storage.googleapis.com/openimages/web/factsfigures_v4.html).

## Object Detection Model
SSD-based object detection model trained on Open Images V4 with ImageNet pre-trained MobileNet V2 as image feature extractor.  
  
The model used for object detection can be found [here](https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1).


## Inference Time
/static/img/Screenshot 2021-05-04 at 11.12.34 PM.png  
Inference time: 8.116887092590332  
  
/static/img/The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpeg  
Inference time: 7.186975955963135   
  
static/img/1024px-Biblioteca_Maimónides,_Campus_Universitario_de_Rabanales_007.jpeg  
Inference time: 7.669946193695068





