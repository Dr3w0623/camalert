import cv2 
import time
stream = cv2.VideoCapture(0) 
def motion_checker():
    is_motion = False
    while(is_motion==False):
        isFrame, frame = stream.read()
        cv2.imshow('cum', frame)
        cv2.waitKey(1)


motion_checker()