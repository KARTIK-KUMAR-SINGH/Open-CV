import cv2

image = cv2.imread("python_image.jpg")

if image is None :
    print("image is not loaded")
else :
    print("image is loaded")
    resize_original = cv2.resize(image , (800 , 600))
    cv2.imshow("image showing" , resize_original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    saving_original = cv2.imwrite("original_image.jpg" , image)
    print("original image saved sucessfully")

    grayscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    resize_grayscale = cv2.resize(grayscale_image , (800 , 600))
    cv2.imshow("grayscale image showing" , resize_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    saving_grayscale = cv2.imwrite("Original_Grayscale.jpg" , grayscale_image)
    print("grayscale image saved sucessfully")