# Smart Lane Detection System

In an era where road safety and driving efficiency are paramount, this project focuses on developing a versatile vehicle lane detection system. Our lane detection system project focuses on making driving safer and more efficient. It's creating a system that can detect lanes on the road, help drivers stay in their lanes, and also spot pedestrians and potholes. The aim is to create a system that improves road safety and shows how advanced technology can make driving safer and easier. The goal is to create a comprehensive solution that enhances road safety and demonstrates the potential of cutting-edge technology in redefining modern transportation.​

The problem to be solved in this project is to enhance road safety, driving efficiency, and promote the adoption of self-driving cars and buses in India. The project's main goal is to make Indian roads safer, help people drive more efficiently, and encourage the use of self-driving vehicles. They plan to do this by creating a system that can detect lanes, pedestrians, and potholes. This system will give real-time information to drivers, helping them avoid accidents and stay in their lanes. 

![MicrosoftTeams-image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/91ad85ac-da2e-428d-a8c2-904c8309003e)
The above figure shows our basic architecture of our entire system. We would like to propose a GPS system to keep a track of the number of potholes at different locations. This would tremendously help the road maintenance authorities to keep a tab of roads which need maintenance. Apart from this, it would encourage accountability from the authorities to take quick action for the same


## Process
The below image shows in-depth process flow of our project.
![MicrosoftTeams-image (1)](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/5dc89e22-3cc8-4637-938c-25e587ea0f4a)

### Lane Detection
We present a Real-Time Road Lane Detection algorithm, which plays a crucial role in ensuring the safe navigation of self-driving cars by accurately identifying lane boundaries. Lane recognition algorithms are fundamental components for both Advanced Driver Assistance Systems ADAS) and autonomous vehicle systems. The steps are given below:
- Sobel Filter​: The Sobel operator performs a 2-D spatial gradient measurement on an image and so emphasizes regions of high spatial frequency that correspond to edges.​ Sobel filter makes use of the following kernels for gradient computation.
  
![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/9f32b5af-17cb-485f-9fda-3b8c0563b66d)

- Canny Edge Detector: It is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.​
  - Non-max suppression: Ideally, the final image should have thin edges.The principle is simple: the algorithm goes through all the points on the gradient intensity matrix and finds the pixels with the maximum value in the edge directions.​
    
    ![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/fde894d5-d24a-4553-9d8d-bb0e522f98ae)

  - Double Thresholding: The gradient magnitudes are compared with two specified threshold values, the first one is lower than the second. The gradients that are smaller than the low threshold value are suppressed, the gradients higher than the high threshold value are marked as strong ones​

- Perspective Transformation: Transformation is the transfer of an object e.t.c from one state to another. So overall, the perspective transformation deals with the conversion of 3d world into 2d image.​ In this case, we are getting a bird’s eye view of the region of interest(road) to fit lanes onto it.

- Lane Fitting: We fit lane lines using the bird’s eye view of the road. ​

  ![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/f4d4b3b5-68cc-4b25-82c9-736f2226308b)

  **OUTPUT**
  ![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/09606996-871e-43f5-b24e-702f9c02a425)


### Object Detection: 
We are using MobileNet SSD trained on the COCO dataset for object detection. MobileNet is a family of convolutional neural network (CNN) architectures that are designed to be efficient and lightweight, making them ideal for mobile and embedded devices. MobileNets can be used for a variety of tasks, including image classification, object detection, and segmentation For object detection, MobileNets are often used as the backbone of a single shot detector (SSD). SSDs are a type of object detector that can detect objects in an image in a single pass. SSDs work by first extracting features from the image using a CNN backbone. Then, the SSD uses these features to predict the bounding boxes and classes of the objects in the image. MobileNet-based SSDs are particularly wellsuited for mobile and embedded devices because they are efficient and lightweight. For example, the MobileNet SSD v2 model is only 267 layers deep and has 15 million parameters, making it much smaller and faster than other object detection models, such as Faster R-CNN.

**OUTPUT**
![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/1da7eae6-7407-476b-b0d3-14d95dc52010)


### Pothole Detection:
The detection of potholes is a critical aspect of our integrated lane and pothole detection system. Potholes pose a significant safety hazard to road users and can lead to infrastructure damage. To address this issue, we employed a YOLOv8 model pre-trained on the COCO dataset, customized and fine-tuned for pothole detection.

**OUTPUT**

![image](https://github.com/sammyboi1801/Smart-Lane-Detection-System/assets/80597420/7ab019b3-8fa2-48a4-8cfc-7c8fa484124b)

## Code
1) Make sure to download the weights for YOLOv8 here: https://www.dropbox.com/scl/fi/q5d9ru21ozn93y6lmyzaz/y8best.pt?rlkey=y4bvfrlu928gb9gkv4w6lgsor&dl=0 . Download it inside the same directory where all the .py files are.
2) In order to run the lane detection along with object detection, run the "lane detection.py" file. This would run the lane detection algorithm along with object detection on a live video stream.
3) In order to run the pothole detection system, run the "pothole detection.py file. This would detect potholes on live video stream.

_Project by Sam Selvaraj, Archisha Srivastava and Rajat Saboo._

Thank you:)




  




​

​

​

​

​

​


