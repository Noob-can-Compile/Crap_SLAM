import cv2
import numpy as np

class Extractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create(100)
        self.bf = cv2.BFMatcher()
        self.last = None

    def extract(self, img):
        fts = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8),3000, qualityLevel = 0.01, minDistance = 1)
        
        kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in fts]
        kps, des = self.orb.compute(img, kps)

        matches = None
        if self.last is not None:
            matches = self.bf.match(des, self.last['des'])
            

        self.last = {'kps' : kps, 'des' : des}
        return kps, des, matches
