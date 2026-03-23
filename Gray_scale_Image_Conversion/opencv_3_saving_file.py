import cv2

image = cv2.imread("python_image.jpg")

if image is None :
    print("image is not loaded") 
else :
    print("image is loaded")
    resize = cv2.resize(image , (800,600))
    cv2.imshow("image showing" , resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    saving = cv2.imwrite("Output.jpg" , image)
    if saving :
        print("image is getting saved")
    else :
        print("image is not saved")