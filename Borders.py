import cv2

image1 = cv2.imread("Images/Gorilla.jpg", 1)
image2 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
image3 = cv2.imread("Images/Passport_Photo.jpg", 1)
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

ThickBorder = cv2.copyMakeBorder(image1, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value = 0.5)
#The 50's make the borders thicker.
cv2.imshow("Thick border", ThickBorder)

cv2.waitKey(0)

ReflectiveBorders = cv2.copyMakeBorder(image3, 50, 50, 50, 50, cv2.BORDER_REFLECT, value = 1)
#This makes the border reflect the image back on itself.
cv2.imshow("Reflective border", ReflectiveBorders)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows