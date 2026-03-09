import cv2

image = cv2.imread("python_image.jpg")

if image is None :
    print("image not loaded")

else :
    print("image loaded sucessfully")
    resize = cv2.resize(image , (800,600))
    cv2.imshow("image showing" , resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()