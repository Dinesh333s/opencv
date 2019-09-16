#video show ,write,read
import  cv2

cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'MPEG')#its 4byte specify video codec
out=cv2.VideoWriter('out.avi', fourcc, 20.0, (640,480))#save the captured video
print(cap.isOpened()) #isOpened class return true or false
a=1
while( cap. isOpened()):
    a=a+1
    ret, frame=cap.read() #two variable =capture read() class
    print(frame)
    if ret == True:

       grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert grey scale image
       cv2.imshow('frame', grey) #show the frame
       out.write(frame)#save the video formats
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #find the width 640
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #find the height 480
       print(a)

       if cv2.waitKey(1) & 0xFF == ord('q'):#0xFF mask for 64 bit system
        break;

    else:
        break
cap.release() #its important its was release the vdo caoture
cv2.destroyAllWindows()


