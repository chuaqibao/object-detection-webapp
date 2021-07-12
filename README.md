# Simple Object Detection Web-app

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
![Screenshot 2021-05-04 at 11 12 34 PM](https://user-images.githubusercontent.com/62118373/125259608-0ebbf100-e332-11eb-8290-900a0b8ebba8.png)

## List of Detectable Objects

List of objects classes can be found [here](https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv).  
Information about the dataset the detector is trained on can be found [here](https://storage.googleapis.com/openimages/web/factsfigures_v4.html).

## Object Detection Model
SSD-based object detection model trained on Open Images V4 with ImageNet pre-trained MobileNet V2 as image feature extractor.  
  
The model used for object detection can be found [here](https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1).



