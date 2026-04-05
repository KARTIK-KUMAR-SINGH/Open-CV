import cv2 

image = cv2.imread("with_median_blur.jpg")

without_blur = cv2.medianBlur(image , 11)

cv2.imshow("Original Image" , image)
cv2.imshow("New Image" , without_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
