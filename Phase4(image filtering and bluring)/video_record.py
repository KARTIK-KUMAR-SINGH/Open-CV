import cv2 

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("vedio_recording.avi" , codec , 20 , (frame_width , frame_height))

while True : 
    ret , frame = cap.read()

    if not ret :
        print("Vedio Frame capture unsucessfull")
        break
    
    recorder.write(frame)
    cv2.imshow("recording vedio" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        print("quitting")
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()
