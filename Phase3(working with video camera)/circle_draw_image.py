import cv2

image = cv2.imread("image.jpg")

if image is not None :
    (h , w) = image.shape[ : 2]
    centre = (w//2 , h//2)
    radius = 100
    color = (255 , 0 , 0)
    thickness = -1
    cv2.circle(image , centre , radius , color , thickness)

    cv2.imshow("circle in the image" , image)
    cv2.waitKey()
    cv2.destroyallWindows()