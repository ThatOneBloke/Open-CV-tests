import cv2

image1 = cv2.imread("Images/Dots.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

Grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#the image needs to be greyscaled before they can be detected
Blurred = cv2.blur(Grey, (3, 3))
#then the image needs to be blurred too
Detected_Circles = cv2.HoughCircles(Blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
#HoughCircles is used to detect circular shapes in image, it uses a technique where it finds and returns the centre and radius of the circle. Blurred is the blurred and greyscaled images, which it works best in as it reduces unnecessary obstructions (image noise). HOUGH_GRADIENT is the function/keyword. Number 1 is the resolution which means 100% (2 = 50%). Number 20 is the minimum pixel distance between two detected circles, which stops overlapping circles from being detected. Param1 is a threshold value, which allows for any larger size circle to be detected. Param2 works the same but allowing allowing any smalled sized circles to be detected. minRadius is as the name suggests, and so is maxRadius (these could be changed at will)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows