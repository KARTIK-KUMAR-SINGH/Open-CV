import cv2

def record_video() :
    camera = cv2.VideoCapture(0)

    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'XVID')
    recorder = cv2.VideoWriter("user_demand_recording2.avi" , codec , 30 , (frame_width , frame_height))

    while True :
        ret , frame = camera.read()

        if not ret :
            print("Video frame capture failed")
            break

        recorder.write(frame)
        cv2.imshow("Recording Video" , frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            print("Quitting....turning of the record")
            break
    camera.release()
    recorder.release()
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

while True :

    ret , frame = cap.read()

    if not ret :
        print("Vedio frame capture unsucessfull")
        break
    
    cv2.imshow("Live Preview before recording" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

print(cap.get(cv2.CAP_PROP_FPS))
cap.release()
cv2.destroyAllWindows()

user_record = input("Do you want to record vedio (Yes/No) :-")
record = user_record.lower()

if (record == 'yes') :
    record_video()

elif (record == 'no') :
    print ("Quitting....No record of vedio done")

else :
    print("Ivalid input re run the code ")
