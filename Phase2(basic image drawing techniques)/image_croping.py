import cv2

image = cv2.imread("original_image.jpg")
resize = cv2.resize(image , (200 , 200))

if image is not None :
    cropped = resize[100 : 200 , 50 : 150]
    cv2.imshow("original Image" , resize)
    cv2.imshow("Original Image" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
