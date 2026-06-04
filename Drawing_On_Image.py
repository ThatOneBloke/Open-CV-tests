import cv2

image1 = cv2.imread("Images/London_Eye.jpg", 1)
image2 = cv2.imread("Images/Passport_Photo.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
cv2.imshow("Second Image", image2)
#shows the image with a window title

cv2.waitKey(0)

StartingPoint = (200, 200)
EndingPoint = (370, 200)
#This gives the starting point and ending point of the line which will be drawn
Colour = (0, 0, 255)
#the colour of the line
Thickness = 5
#how thick the line is
image1 = cv2.line(image1, StartingPoint, EndingPoint, Colour, Thickness)
#This creates the line on the image.

cv2.imshow("Drawn On Image", image1)

cv2.waitKey(0)

StartingPoint = (90, 190)
EndingPoint = (250, 240)
Colour = (0, 0, 0)
Thickness = 5
image2 = cv2.rectangle(image2, StartingPoint, EndingPoint, Colour, Thickness)
#This creates a rectange on the image.

cv2.imshow("Rectangle On Image", image2)

cv2.waitKey(0)

StartingPoint = (90, 190)
EndingPoint = (250, 240)
Colour = (0, 0, 0)
Thickness = -1
image2 = cv2.rectangle(image2, StartingPoint, EndingPoint, Colour, Thickness)
#Due to the -1 thickness, the rectangle will be shaded in.

cv2.imshow("Shaded Rectangle On Image", image2)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows