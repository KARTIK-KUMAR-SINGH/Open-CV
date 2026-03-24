import cv2

image = cv2.imread("image.jpg")

if image is not None :
    pt1 = (50 , 100)
    pt2 = (300 , 100)
    color = (255 , 0 , 0)
    thickness = 4


    cv2.line(image , pt1 , pt2 , color , thickness)

    cv2.imshow("image with the line" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
