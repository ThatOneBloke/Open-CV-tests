import cv2

image1 = cv2.imread("Images/Gorilla.jpg", 1)
image2 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
cv2.imshow("Second Image", image2)
#shows the image with a window title

cv2.waitKey(0)

borderedImage1 = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
#This will create a border. the four 10's are the thicknes of each border.Top, Left, Bottom, Right. This makes sure the border stays. value = 1 means it is equal ratio between all the borders.
borderedImage2 = cv2.copyMakeBorder(image2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow("Bordered Image One", borderedImage1)
cv2.imshow("Bordered Image Two", borderedImage2)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows