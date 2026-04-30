import cv2

image1 = cv2.imread("Images/Fox.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

#it will hold the window until the user presses a key
image2 = cv2.imread("Images/Fox.jpg", 0)
#Due to the zero, there will be no colour in the image. 1 means there will be
cv2.imshow("Grey Scale Image", image2)

cv2.waitKey(0)

cv2.destroyAllWindows()
#it will destroy all windows