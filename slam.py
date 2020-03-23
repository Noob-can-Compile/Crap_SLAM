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
    kp, des, matches = fe.extract(img)
    if matches is None:
        return

    for point in kp:
        u,v = map(lambda x: int(round(x)), point.pt)
        cv2.circle(img, (u,v), color = (0,255,0), radius = 1, thickness = 2)
    
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("car.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frames_per_motion(frame)
        else:
            break
    