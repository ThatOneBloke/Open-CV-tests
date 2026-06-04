import cv2

image1 = cv2.imread("Images/London_Eye.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

CentreCoords = (285, 200)
Radius = 120
#The two variables replace starting and ending point as a circle needs a centre point and a radius instead
Colour = 0, 0, 255
Thickness = 5

image1 = cv2.circle(image1, CentreCoords, Radius, Colour, Thickness)
#This is how to make a circle.

cv2.imshow("Circle On Image", image1)

cv2.waitKey(0)

CentreCoords = (285, 200)
Radius = 120
Colour = (0, 0, 255)
Thickness = -1

image1 = cv2.circle(image1, CentreCoords, Radius, Colour, Thickness)

cv2.imshow("Filled Circle On Image", image1)

cv2.waitKey(0)

Font = cv2.FONT_HERSHEY_COMPLEX
#this decides the font of the letters. I don't know what font this is.
StartingPoint = (200, 200)
FontScale = 1
#it is 100% of the size of the font. 
Colour = (255, 0, 0)
Thickness = 3
image1 = cv2.putText(image1, "London Eye", StartingPoint, Font, FontScale, Colour, Thickness)

cv2.imshow("Text On Image", image1)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows