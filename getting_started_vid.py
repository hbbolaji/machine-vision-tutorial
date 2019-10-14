# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
# # for x in np.arange(1, 19):
# #     print(cap.get(x))
# cap.set(3, 320)
# cap.set(4, 240)
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('images/vidcam.avi', fourcc, 20, (640, 480))
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.flip(frame, 0)
#     out.write(gray)
#     cv2.imshow('Video Captured', gray)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# out.release()
# cap.release()
# cv2.destroyAllWindows()

import numpy as np
import cv2

cap = cv2.VideoCapture('images/vidcam.avi')
cap.set(3, 640)
cap.set(4, 480)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.flip(frame, 0)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
