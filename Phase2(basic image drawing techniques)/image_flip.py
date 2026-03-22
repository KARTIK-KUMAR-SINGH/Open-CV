import cv2

image = cv2.imread("image.jpg")

if image is not None :
    fliped_0 = cv2.flip(image , 0)
    fliped_1 = cv2.flip(image , 1)
    fliped_minus_1 = cv2.flip(image , -1)
    
    cv2.imshow("original image" , image)
    cv2.imshow("Top to bottom" , fliped_0)
    cv2.imshow("Left to right" , fliped_1)
    cv2.imshow("both" , fliped_minus_1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()