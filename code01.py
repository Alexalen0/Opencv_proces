# py -m pip install opencv-python
import cv2 as cv
import numpy as np
import sys

img = cv.imread(cv.samples.findFile("rose.jpg"))
img_color = cv.imread('rose.jpg', cv.IMREAD_COLOR)              #1
img_grayscale = cv.imread('rose.jpg', cv.IMREAD_GRAYSCALE)      #0
img_unchanged = cv.imread('rose.jpg', cv.IMREAD_UNCHANGED)      #-1

if img is None:
    sys.exit("Could not read the image.")
if img_grayscale is None:
    sys.exit("Could not read the image.")
if img_color is None:
    sys.exit("Could not read the image.")
if img_unchanged is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
cv.imshow("img_color", img_color)
cv.imshow("img_grayscale", img_grayscale)
cv.imshow("img_unchanged", img_unchanged)

cv.waitKey(0)
cv.destroyAllWindows()