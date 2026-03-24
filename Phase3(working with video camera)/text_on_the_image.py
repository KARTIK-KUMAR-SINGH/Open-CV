import cv2

image = cv2.imread("image.jpg")

if image is not None :
    text = "Hello Everyone"
    org = (150,100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1.5
    color = (255 , 0 , 0)
    thickness = 4
    cv2.putText(image , text , org , font , fontscale , color , thickness)
    cv2.imshow("Circle in the image" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()