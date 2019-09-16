#handle mouse event
import cv2
import numpy as np
#dir is a inbuild function

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):


    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x) +','+ str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('dinesh',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) +', ' +str(green)+', '+str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (161, 56, 25), 1)
        cv2.imshow('dinesh', img)

#img = np.zeros((512,512,3),np.uint8)
img=cv2.imread('/home/dinesh/Documents/hello/lena.jpg',1)
cv2.imshow('dinesh',img)


cv2.setMouseCallback('dinesh', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()