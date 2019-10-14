import numpy as np
import cv2

img = cv2.imread('images/bird.jpg', cv2.IMREAD_ANYCOLOR)
cv2.imshow('Bird Image', img)
cv2.waitKey()
cv2.destroyAllWindows()