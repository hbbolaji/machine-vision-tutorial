import numpy as np
import cv2

img = cv2.imread('data/basketball1.png', cv2.IMREAD_ANYCOLOR)
cv2.namedWindow('Basketball Image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Basketball Image', img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/newbasketball.png', img)
    cv2.destroyAllWindows()