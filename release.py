# Python program to implement
# Webcam Motion Detector

# importing OpenCV, time and Pandas library
import cv2, time, pandas
# importing datetime class from datetime library
from datetime import datetime

# Assigning our static_back to None
static_back = None

# List when any moving object appear
motion_list = [ None, None ]

cap = cv2.VideoCapture(1)
while(cap.isOpened()):
      
    while True:
          
        ret, img = cap.read()
        cv2.imshow('img', img)
        if cv2.waitKey(30) & 0xff == ord('q'):
            break
              
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Alert ! Camera disconnected")

