# import cv2
# image = cv2.imread("original_image.jpg")
# if image is None :
#     print("Image not found")
# else :
#     print("Image is now found")
#     resized = cv2.resize(image , (800 , 600))
#     cv2.imshow("Image is now showing" , resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     cv2.imwrite("revision.png" , image)

# import cv2
# image1 = cv2.imread("original_image.jpg")
# image2 = cv2.imread("Original_Grayscale.jpg")

# if image1 is not None :
#     h1 , w1 , c1 = image1.shape
#     print(f"Image Loaded : \nHeight {h1}\nWidth {w1}\nChannels {c1}")
# if image2 is not None :
#     h2 , w2 , c2 = image2.shape
#     print(f"Image Loaded : \nHeight {h2}\nWidth {w2}\nChannels {c2}")

import cv2
image = cv2.imread("original_image.jpg")

if image is not None : 
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(gray , (800 , 600))
    cv2.imshow("Grayscale image" , resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
