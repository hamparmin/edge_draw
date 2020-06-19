 
import cv2
import os
import numpy as np

# Load images
def image_make(path):
	img = cv2.imread(path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 60, 120)
	invert=cv2.bitwise_not(edges)
	return cv2.imencode(".jpg",invert)