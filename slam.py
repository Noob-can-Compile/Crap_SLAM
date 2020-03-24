import time
import cv2
import numpy as np
from display import Display
from extractor import Extractor

width = 1280//2  #1920//2
height = 720//2  #1080//2   

disp = Display(width, height)
fe = Extractor()

def frames_per_motion(img):
    img = cv2.resize(img, (width, height))
    matches = fe.extract(img)
    
    print("%d matches" % (len(matches)))

    for point1, point2 in matches:
        u1,v1 = map(lambda x: int(round(x)), point1)
        u2,v2 = map(lambda x: int(round(x)), point2)
        cv2.circle(img, (u1,v1), color = (0,255,0), radius = 1, thickness = 2)
        cv2.line(img, (u1,v1), (u2,v2), color = (255,0,0))
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("videos/car4.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frames_per_motion(frame)
        else:
            break
    