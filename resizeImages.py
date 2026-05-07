import cv2

image1 = cv2.imread("Images/Fox.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

reduceSize = cv2.resize(image1, (200, 200))
#this will reduce the size of the image. It is width then height --> (WIDTH, HEIGHT)
cv2.imshow("reduced image", reduceSize)

increaseSize = cv2.resize(image1, (800, 500))
#this will increase the size of the image
cv2.imshow("increased image", increaseSize)

stretchedSize = cv2.resize(image1, (1000, 100))
tallSize = cv2.resize(image1, (200, 600))
#this will stretch the image instead of adding a black outline
cv2.imshow("stretched image", stretchedSize)
cv2.imshow("tall image", tallSize)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows