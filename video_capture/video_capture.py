import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print "Open Success"
    # read frame
    success, frame = cap.read()
    while success:
        cv2.imshow("Oto Video", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break        
        success, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
else:
    print "Open False"