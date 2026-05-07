import cv2

image1 = cv2.imread("Images/Fox.jpg", 1)
image2 = cv2.imread("Images/London_Eye.jpg", 1)
image3 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
image4 = cv2.imread("Images/Gorilla.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
cv2.imshow("Second Image", image2)
cv2.imshow("Third Image", image3)
cv2.imshow("Fourth Image", image4)
#shows the image with a window title

cv2.waitKey(0)

Subtract1 = cv2.subtract(image1, image2)
#it reverses the colours of the Second image onto the first image. Hard to explain check yourself.
cv2.imshow("First images subtracted by Second image", Subtract1)

cv2.waitKey(0)

Subtract2 = cv2.subtract(image2, image1)
cv2.imshow("First images subtracted by Second image", Subtract2)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows