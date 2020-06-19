 
import cv2
import os
import numpy as np

# Load images
def image_make(file_name):
	folder='uploads'

	img = cv2.imread(os.path.join(folder,file_name))

	# Converting the image to grayscale.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Canny Filter
	edges = cv2.Canny(gray, 60, 120)

	#Invert color
	invert=cv2.bitwise_not(edges)

	cv2.imwrite(os.path.join(folder,file_name),invert)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()