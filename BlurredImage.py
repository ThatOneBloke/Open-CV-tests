import cv2

image1 = cv2.imread("Images/Passport_Photo.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)
#it will hold the window until the user presses a key

Gaussian = cv2.GaussianBlur(image1, (7, 7), 0)
#This will blur the image, but differently to the the errosion, as the pixels are not enlarged, just less defined. This is used in machine learning - preprocessing steps
cv2.imshow("Gaussian blur", Gaussian)

cv2.waitKey(0)

Median = cv2.medianBlur(image1, 5)
#It blurs the image from the centre, which is the centre (there are 4 corners, the fifth is the centre). Think of it as more of a middle blur than a huge blur.
cv2.imshow("Median blur", Median)

cv2.waitKey(0)

Bilateral = cv2.bilateralFilter(image1, 9, 75, 75)
#It blurs everything but the sharp edges. the 9 signifies the size of the pixel. the two 75's are the rows and columns that the image is divided into.
cv2.imshow("Bilateral Blur", Bilateral)

cv2.waitKey(0)

cv2.destroyAllWindows()
#it will destroy all windows