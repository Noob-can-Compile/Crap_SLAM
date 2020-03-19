import numpy as np
import cv2

width = 1280//2 
height = 720//2
def frames_per_motion(img):
    img = cv2.resize(img, (width, height))
    cv2.imshow("image", img)
    cv2.waitKey(1)
    print(img.shape)
    print(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("car.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frames_per_motion(frame)
        else:
            break
    