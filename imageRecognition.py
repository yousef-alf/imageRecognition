# import the necessary packages
import numpy as np
import argparse
import cv2
img = cv2.imread("bluered.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([110, 50,50])
upper_range = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow("image", img)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

