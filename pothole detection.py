from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2
# model = YOLO("y8best.pt")
# results = model.predict(source="tested.mp4", show=True)
# print(results)

import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLOv8 model
model = YOLO("y8best.pt")

# Open the video file
video_path = "output_vid/pothole2.mp4"
cap = cv2.VideoCapture(video_path)

classes = {0: 'BAD_BILLBOARD', 1: 'BROKEN_SIGNAGE', 2: 'CLUTTER_SIDEWALK', 3: 'CONSTRUCTION_ROAD', 4: 'FADED_SIGNAGE', 5: 'GARBAGE', 6: 'GRAFFITI', 7: 'POTHOLES', 8: 'SAND_ON_ROAD', 9: 'UNKEPT_FACADE'}
font_scale = 2
font = cv2.FONT_HERSHEY_PLAIN

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(frame)
        # # Visualize the results on the frame
        # frame = results[0].plot()


        for result in results:
            boxes = tuple(np.array(result.boxes.xyxy))  # Boxes object for bbox outputs
            # print(result.boxes.conf)
            predclass = tuple(np.array(result.boxes.cls))
            confidence = tuple(np.array(result.boxes.conf))

            for cl,box,conf in zip(predclass,boxes,confidence):
                # print(box)
                b0,b1,b2,b3 = box[0],box[1],box[2],box[3]
                cv2.rectangle(frame, (int(b0),int(b1)),(int(b2),int(b3)), (255, 0, 0), 2)
                if cl==5.:
                    # cv2.rectangle(frame, (100,200),(300,400), (255, 0, 0), 2)
                    cv2.putText(frame, classes[7]+" "+str(int(100*conf))+"%", (int(b0) - 10, int(b1)-10), font,
                                fontScale=font_scale, color=(0, 255, 0), thickness=2)
                else:
                    cv2.putText(frame, classes[int(cl)]+" "+str(int(100*conf))+"%", (int(b0) - 10, int(b1) - 10), font,
                                fontScale=font_scale, color=(0, 255, 0), thickness=2)

                # print(cl)


        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
