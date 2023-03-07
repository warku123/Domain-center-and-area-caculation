import numpy as np
import cv2

img = np.random.randint(0, 2, size=(10, 10))

cv2.imwrite("test_bin.png", img*255)