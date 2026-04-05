import cv2
import numpy as np 

image = cv2.imread("unsharpen_image.jpg")

kernel = np.array([
    [0 , -1 , 0],
    [-1 , 5 , -1],
    [0 , -1 , 0]
])

sharpen_image = cv2.filter2D(image , -1 , kernel)

cv2.imshow("Original Image" , image)
cv2.imshow("sharpened _image" , sharpen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()