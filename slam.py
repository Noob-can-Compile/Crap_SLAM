import time
import cv2
from display import Display


width = 1280//2 
height = 720//2

disp = Display(width, height)
orb = cv2.ORB_create()


def frames_per_motion(img):
    img = cv2.resize(img, (width, height))
    kp, des = orb.detectAndCompute(img,None)
    for keypoint in kp:
        u,v = map(lambda x: int(round(x)), keypoint.pt)
        cv2.circle(img, (u,v), color = (0,255,0), radius = 3, thickness = 2)
    disp.paint(img)
    #cv2.imshow("image", img)
    #cv2.waitKey(1)
    #print(img.shape)
    #print(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("car.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frames_per_motion(frame)
        else:
            break
    