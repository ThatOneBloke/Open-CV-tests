import cv2
import numpy as np

image1 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)
#it will hold the window until the user presses a key

imageGraph = np.ones((10, 10), np.uint8)
#divides the data(image) into a 2d array with rows and columns that all are equal to one. The number of rows and columns are shown in the brackets (10, 10). Uint means unified intiger. It takes 8 bits to store the data

finalImage = cv2.erode(image1, imageGraph)
#Erode means the pixels will be enlarged to create a more blurry image. Internally the corners are trimmed.

cv2.imshow("Eroded image", finalImage)

cv2.waitKey(0)

cv2.destroyAllWindows()
#it will destroy all windows