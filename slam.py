import time
import cv2
import numpy as np
from display import Display

width = 1280//2  #1920//2
height = 720//2  #1080//2   

disp = Display(width, height)

class FeatureExtractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create(100)
        self.bf = cv2.BFMatcher()
        self.last = None

    def extract(self, img):
        fts = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8),3000, qualityLevel = 0.01, minDistance = 1)
        kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in fts]
        kps, des = self.orb.compute(img, kps)

        if self.last is not None:
            matches = self.bf.match(des, self.last['des'])
            print(matches)

        self.last = {'kps' : kps, 'des' : des}
        return kps, des

fe = FeatureExtractor()

def frames_per_motion(img):
    img = cv2.resize(img, (width, height))
    kp, des = fe.extract(img)

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
    