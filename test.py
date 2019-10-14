import numpy as np
import cv2

cap = cv2.VideoCapture('images/output.avi')

while (cap.isOpened()):
    ret, frame = cap.read()
    framedVid = cv2.flip(frame, 1)
    cv2.imshow('our video', framedVid)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
