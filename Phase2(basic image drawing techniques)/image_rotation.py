import cv2

image = cv2.imread("original_image.jpg")

if image is not None :
    resize = cv2.resize(image , (800 ,600))

    (h , w) = resize.shape[ : 2]
    centre = (w//2 , h//2)

    M = cv2.getRotationMatrix2D(centre , 90 , 0.5)
    rotated = cv2.warpAffine(resize , M , (w , h))

    # resize_rotated = cv2.resize(rotated , (800 ,800))

    cv2.imshow("resized image" , resize)
    cv2.imshow("resize_rotated image" , rotated)
    # cv2.imshow("resize_rotated image" , resize_rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()