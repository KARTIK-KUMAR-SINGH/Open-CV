import cv2

image = cv2.imread("python_image.jpg")

if image is None :
    print("image not found")
else :
    print("image loaded sucessfully")