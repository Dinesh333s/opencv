#show date and time on video

import cv2
import datetime #display the date and time on video

cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,3000)
#cap.set(4,3000)
#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):

    ret,frame= cap.read()
    if ret == True:

         font = cv2.FONT_HERSHEY_SIMPLEX
         text = 'Width:' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
         #datetime.datetime.now() is inbuild method of datetime
         datet = str(datetime.datetime.now())
         cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
         cv2.imshow('dinesh',frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break

cap.release()
cv2.destroyAllWindows()