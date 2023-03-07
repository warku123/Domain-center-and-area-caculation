import numpy as np
import cv2

img = cv2.imread('pic7.png')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# cv2.imwrite("pic6_grey.png", img)

ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

cv2.imwrite("pic7_bin.png", thresh)