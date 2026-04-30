import cv2
import numpy as np
#Numpy is short for numberical python. It has ready-made functions for calculations. NP is the nickname which can be used for it.

image1 = cv2.imread("Images/Fox.jpg")
cv2.imshow("Fox", image1)

B, G, R = cv2.split(image1)
#this splits the image into BGR, or Blue Green Red (RGB flipped).
blank = np.zeros_like(B)
#this creates a blank list of zeroes.
blueImage = cv2.merge([B, blank, blank])
#this will make the other two (Green and Red) to become 000, which means they will not be part of the image.
greenImage = cv2.merge([blank, G, blank])
#this will do the same as blueImage, except the image will only be green
redImage = cv2.merge([blank, blank, R])
#this will do the same as BlueImage and greenImage, except the image will only be red

cv2.imshow("Blue Only", blueImage)
cv2.imshow("Green Only", greenImage)
cv2.imshow("Red Only", redImage)

cv2.waitKey(0)
cv2.destroyAllWindows()