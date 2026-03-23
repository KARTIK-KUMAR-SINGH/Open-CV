import cv2

image = cv2.imread("python_image.jpg")

if image is not None :
    print("Image loaded sucessfully")
    h , w , c = image.shape
    print("height of the image" , h)
    print("widht of the image" , w)
    print("colour channel of the iamge" , c)
else :
    print("image not loaded sucessfully")
