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

# Time of movement
time = []

# Initializing DataFrame, one column is start
# time and other column is end time
df = pandas.DataFrame(columns = ["Start", "End"])

# Capturing video and initializing camera, change index to find your camera
video = cv2.VideoCapture(1)
video2 = cv2.VideoCapture(0)

video.release()
video2.release()

# Destroying all the windows
cv2.destroyAllWindows()

