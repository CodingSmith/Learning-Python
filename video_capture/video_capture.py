import numpy as np
import cv2

cap = cv2.VideoCapture(r'/home/slingman/project_codes/Python/data/video/slow.flv')

if cap.isOpened():
    print "Open Success"
    # get fps
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    # read frame
    success, frame = cap.read()
    while success:
        cv2.imshow("Oto Video", frame)
        cv2.waitKey(1000 / int(fps))
        success, frame = cap.read()
else:
    print "Open False"