import cv2
image = cv2.imread("original_image.jpg")

if image is not None :
    cv2.imshow("not rescaled image" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

resized = cv2.resize(image , (800 , 600))
if resized is not None :
    cv2.imshow("resized image" , resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
