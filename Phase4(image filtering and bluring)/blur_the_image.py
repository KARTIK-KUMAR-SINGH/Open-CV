import cv2

image = cv2.imread("image.jpg")

blured = cv2.GaussianBlur(image , (7,7) , 6)

cv2.imshow("Original Image" , image)
cv2.imshow("Blured Image" , blured)
cv2.waitKey(0)
cv2.destroyAllWindows()
