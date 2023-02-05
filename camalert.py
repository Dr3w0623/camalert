import cv2 
import time
import statistics

stream = cv2.VideoCapture(0) 

def motion_checker():
    while(True):
        is_frame, frame = stream.read()
        if is_frame != True: break
        is_frame, comp_frame = stream.read()
        frame_difference = cv2.absdiff(frame, comp_frame)
        frame_gray = cv2.cvtColor(frame_difference, cv2.COLOR_BGR2GRAY)
        frame_blur = cv2.GaussianBlur(frame_gray, (5,5), 0)
        frame_thresh = cv2.adaptiveThreshold(frame_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 27, 15)
        frame_dilated = cv2.dilate(frame_thresh, None, iterations=3)
        contours_list, trash = cv2.findContours(frame_dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        biggest_contour_area = 0
        for contour in contours_list:
            if cv2.contourArea(contour) > biggest_contour_area:
                biggest_contour_area = cv2.contourArea(contour)
                big_contour = contour
        (x, y, w, h) = cv2.boundingRect(big_contour)
        stream_width = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
        stream_height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cv2.rectangle(frame, (max(x-20, 0), max(y-20, 0)), (min(x+w+20, stream_width), min(y+h+20, stream_height)), (255, 255, 0), 2)
        show(frame)
        if biggest_contour_area > 500: 
            eventMaker(frame)

def eventMaker(frame):
    print('ah')

def show(frame):
    cv2.imshow('ah', frame)
    cv2.waitKey(1)



motion_checker()