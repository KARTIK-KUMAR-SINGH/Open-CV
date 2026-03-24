import cv2

image_take = input("Enter the file :- ")

image = cv2.imread(image_take)

def line(image , x1 , y1 , x2 , y2 , color , thickness) :
    pt1 = (x1 , y1)
    pt2 = (x2 , y2)
    if(color == "blue") :
        color_user = (255 , 0 , 0)
    elif(color == "green") :
        color_user = (0 , 255 , 0)
    elif(color == "red") :
        color_user = (0 , 0 , 255)
    else :
        print("The Input of the colour was invalid re run the code")
        return 0
    cv2.line(image , pt1 , pt2 , color_user , thickness)
    cv2.imshow("Line on the image preview" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_user = input("Do you Want to save it ? Enter (Yes / NO) :- ")
    save = save_user.lower()
    if(save == "yes") :
        cv2.imwrite("user_gave_line_on_image.jpg" , image)
    elif(save == "no") :
        print("The modified image was not saved")
    else :
        print("Your choice was invalid Please re run the program")

def rectangle(image , x1 , y1 , x2 , y2 , color , thickness) :
    pt1 = (x1 , y1)
    pt2 = (x2 , y2)
    if(color == "blue") :
        color_user = (255 , 0 , 0)
    elif(color == "green") :
        color_user = (0 , 255 , 0)
    elif(color == "red") :
        color_user = (0 , 0 , 255)
    else :
        print("The Input of the colour was invalid re run the code")
        return 0
    cv2.rectangle(image , pt1 , pt2 , color_user , thickness)
    cv2.imshow("Rectangle on the image preview" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_user = input("Do you Want to save it ? Enter (Yes / NO) :- ")
    save = save_user.lower()
    if(save == "yes") :
        cv2.imwrite("user_gave_Rectangle_on_image.jpg" , image)
    elif(save == "no") :
        print("The modified image was not saved")
    else :
        print("Your choice was invalid Please re run the program")

def circle(image , centre , radius , color , thickness) :
     if(color == "blue") :
        color_user = (255 , 0 , 0)
     elif(color == "green") :
        color_user = (0 , 255 , 0)
     elif(color == "red") :
        color_user = (0 , 0 , 255)
     else :
        print("The Input of the colour was invalid re run the code")
        return 0
     cv2.circle(image , centre , radius , color_user , thickness)
     cv2.imshow("Circle on the image preview" , image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     save_user = input("Do you Want to save it ? Enter (Yes / NO) :- ")
     save = save_user.lower()
     if(save == "yes") :
        cv2.imwrite("user_gave_Circle_on_image.jpg" , image)
     elif(save == "no") :
        print("The modified image was not saved")
     else :
        print("Your choice was invalid Please re run the program")

def text(image , x1 , y1 , font_scale , color , thickness) :
    text = input("Enter the Text to write in the image :- ")
    pt1 = (x1 , y1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if(color == "blue") :
        color_user = (255 , 0 , 0)
    elif(color == "green") :
        color_user = (0 , 255 , 0)
    elif(color == "red") :
        color_user = (0 , 0 , 255)
    else :
        print("The Input of the colour was invalid re run the code")
        return 0
    cv2.putText(image , text , pt1 , font , font_scale , color_user , thickness)
    cv2.imshow("Text on the image preview" , image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    save_user = input("Do you Want to save it ? Enter (Yes / NO) :- ")
    save = save_user.lower()
    if(save == "yes") :
        cv2.imwrite("user_gave_text_on_image.jpg" , image)
    elif(save == "no") :
        print("The modified image was not saved")
    else :
        print("Your choice was invalid Please re run the program")

    
    

if image is None :
    print("The file location is not found")
else :
    shape_input = input("Enter the Shape you want to draw or write in the image file(Line , Rectangle , Circle , Text) :- ")
    shape = shape_input.lower()

    if (shape == "line") :
        x1 = int(input("Enter the value of x1 :- "))
        y1 = int(input("Enter the value of y1 :- "))
        x2 = int(input("Enter the value of x2 :- "))
        y2 = int(input("Enter the value of y2 :- "))

        color_input = input("Enter the colour of the line(blue , green , red) :-")
        color = color_input.lower()
        thickness = int(input("Enter the the value of thickness :- "))
        line(image , x1 , y1 , x2 , y2 , color , thickness)

    elif (shape == "rectangle") :
        x1 = int(input("Enter the value of x1 :- "))
        y1 = int(input("Enter the value of y1 :- "))
        x2 = int(input("Enter the value of x2 :- "))
        y2 = int(input("Enter the value of y2 :- "))

        color_input = input("Enter the colour of the line(blue , green , red) :-")
        color = color_input.lower()
        thickness = int(input("Enter the the value of thickness :- "))
        rectangle(image , x1 , y1 , x2 , y2 , color , thickness)

    elif(shape == "circle") :
        (h , w) = image.shape[ : 2]
        centre = (w // 2  , h // 2)
        radius = int(input("Enter The Radius of the circe :- "))
        color_input = input("Enter the colour of the line(blue , green , red) :-")
        color = color_input.lower()
        thickness = int(input("Enter the the value of thickness :- "))
        circle(image , centre , radius , color , thickness)

    elif(shape == "text") :
        x1 = int(input("Enter the value of x1 :- "))
        y1 = int(input("Enter the value of y1 :- "))
        font_scale = float(input("Enter the font scale(0.5 , 1  , 1.5) :- "))
        color_input = input("Enter the colour of the line(blue , green , red) :-")
        color = color_input.lower()
        thickness = int(input("Enter the the value of thickness :- "))
        text(image , x1 , y1 , font_scale , color , thickness)


    else :
        print("The Input was invalid re run the code")

    


