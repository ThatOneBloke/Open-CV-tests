import cv2

image1 = cv2.imread("Images/Gorilla.jpg", 1)
image2 = cv2.imread("Images/Great_Wall_Of_China.jpg", 1)
#Loads the image
cv2.imshow("First Image - Original", image1)
cv2.imshow("Second Image - Original", image2)
#shows the image with a window title

cv2.waitKey(0)

AddedImage1 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
#this will change the image transparency. The 0.5 the transparency which the image will be shown. This allows both the images to be fully seen
cv2.imshow("half of both images", AddedImage1)

cv2.waitKey(0)

AddedImage2 = cv2.addWeighted(image1, 0.75, image2, 0.25, 0)
#this will make the Gorilla image more prominent by 3/4, whilst the other only 1/4
cv2.imshow("3/4 Gorilla, 1/4 Great Wall of China", AddedImage2)

cv2.waitKey(0)

AddedImage3 = cv2.addWeighted(image1, 0.25, image2, 0.75, 0)
#this will do the same as AddedImage2 but make The Great Wall of China more prominent instead
cv2.imshow("1/4 Gorilla, 3/4 Great Wall of China", AddedImage3)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows