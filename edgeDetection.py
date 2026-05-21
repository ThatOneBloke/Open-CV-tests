import cv2

image1 = cv2.imread("Images/Fox.jpg", 1)
image2 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
cv2.imshow("Second Image", image2)
#shows the image with a window title

cv2.waitKey(0)

Edges1 = cv2.Canny(image1, 100, 200)
Edges2 = cv2.Canny(image2, 100, 200)
#100 = lower limit (threshold) 200 = upper limit (threshold). This makes the whole image black, but the edges of the image which are found turn white.
cv2.imshow("Edge Detection", Edges1)
cv2.imshow("Edge Detection on Landscape", Edges2)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows