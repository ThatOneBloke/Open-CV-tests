import cv2
import numpy as np

image1 = cv2.imread("Images/Marbles.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

Grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#the image needs to be greyscaled before they can be detected
Blurred = cv2.blur(Grey, (3, 3))
#then the image needs to be blurred too
Detected_Circles = cv2.HoughCircles(Blurred, cv2.HOUGH_GRADIENT, 1, 10, param1 = 50, param2 = 20, minRadius = 1, maxRadius = 40)
#HoughCircles is used to detect circular shapes in image, it uses a technique where it finds and returns the centre and radius of the circle. Blurred is the blurred and greyscaled images, which it works best in as it reduces unnecessary obstructions (image noise). HOUGH_GRADIENT is the function/keyword. Number 1 is the resolution which means 100% (2 = 50%). Number 20 is the minimum pixel distance between two detected circles, which stops overlapping circles from being detected. Param1 is a threshold value, which allows for any larger size circle to be detected. Param2 works the same but allowing allowing any smalled sized circles to be detected. minRadius is as the name suggests, and so is maxRadius (these could be changed at will)

if Detected_Circles is not None:
    #if there is something in the variable
    Detected_Circles = np.uint16(np.around(Detected_Circles))
    #np.uint(unified intiger) 16 (bits) turns the value into a number, whilst np.around draws the circle around the detected circle
    for i in Detected_Circles[0, :]:
        #the 0 means the first row, : means all the columns. This means the Detected_Circles will check only the first row, but everything inside it.
        x, y, r = i[0], i[1], i[2]
        #in Detecred_Circles, the variables gives back three things. X, Y, and Radius, in a list. the [] with the numbers access these variables in order and placing them in their own variable.
        cv2.circle(image1, (x, y), r, (255, 0, 0), 5)
        cv2.circle(image1, (x, y), 2, (0, 0, 255), 3)

        cv2.imshow("Circles Detected", image1)
        cv2.waitKey(0)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows