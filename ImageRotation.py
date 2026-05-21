import cv2
import numpy as np

image1 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

(rows, columns) = image1.shape[:2]
#the two variables are in one bracket as the ".shape" keyword returns the shape (the rows and columns which the image consumes). The ":2" means the two numbers (rows and columms) will be stored in the variables.

RotationMetrics = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 1)
#This gives the parameter to rotate the image. the (columns/2, rows/2) allows for the centre to be found, whilst the 45 is the degree which it is rotated. The 1 helps rotate evenly.
result = cv2.warpAffine(image1, RotationMetrics, (columns, rows))
#This just allows for the image to be rotated. The (columns, rows) help us rotate, as the RotationMetrics make it easier to rotate

cv2.imshow("Rotated Image", result)

cv2.waitKey(0)

for i in range(0, 360):
    RotationMetrics = cv2.getRotationMatrix2D((columns/2, rows/2), i, 1)
    ClockMovement = cv2.warpAffine(image1, RotationMetrics, (columns, rows))
    cv2.imshow("Spinning Image", ClockMovement)
    cv2.waitKey(0)

for i in range(360, 0, -1):
    RotationMetrics = cv2.getRotationMatrix2D((columns/2, rows/2), i, 1)
    ClockMovement = cv2.warpAffine(image1, RotationMetrics, (columns, rows))
    cv2.imshow("Spinning Image", ClockMovement)
    cv2.waitKey(0)

for i in range(0, 360, 15):
    RotationMetrics = cv2.getRotationMatrix2D((columns/2, rows/2), i, 1)
    ClockMovement = cv2.warpAffine(image1, RotationMetrics, (columns, rows))
    cv2.imshow("Spinning Image", ClockMovement)
    cv2.waitKey(0)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows