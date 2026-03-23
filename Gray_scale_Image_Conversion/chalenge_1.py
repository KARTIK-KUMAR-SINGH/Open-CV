import cv2 

location = input("Enter the image path :----> ")

image = cv2.imread(location)

if image is None :
    print("image not loaded may something error in file location")
else :
    print("image laoded sucessfully\nconverting the image into garyscale")

    grayscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(grayscale_image , (800 , 600))

    option  = input("Enter what you want\nDo you want to only see your grayscale image then write (show) :----> \n Do you want to only save your grayscale image then write(save) :----> \nDo you want to see as well as save your image then write (show_save) :----> ")

    if(option == "show") :
        cv2.imshow("only showing" , resize)
        cv2.waitKey()
        cv2.destroyAllWindows()
        print("only showing")

    elif(option == "save") :
        print("only saving")
        only_save = input("Enter the file name along with the extension you wnat to save the image :----> ")
        cv2.imwrite(only_save , grayscale_image)
        
    elif(option == "show_save") :
        cv2.imshow("showing then saving" , resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image showed sucessfully now saving")
        show_save = input("Enter the file name with which you wnat to save along with the extension :----> ")
        cv2.imwrite(show_save , grayscale_image)

