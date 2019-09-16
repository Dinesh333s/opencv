#geometric shape on image
import numpy as np
import cv2

#create black img using numpy
img = np.zeros([525, 525, 3], np.uint8)
#img = cv2.imread("/home/dinesh/Documents/opencv-master/samples/data/messi5.jpg",1)

#line:we pass 5 arg 1.img 2.start coordinates 3.end coordinates 4.color 5.thickness

img = cv2.line(img, (0, 0), (255, 255), (90, 245, 65), 2)

#arrow line pass 5 arg 1.img 2.start coordinates 3.end coordinates 4.color 5.thickness

img = cv2.arrowedLine(img, (0, 255), (255, 255), (0,255,0),5)

#rectangle
img =cv2.rectangle(img, (384, 0),(510, 128), (255, 0, 0), 10)

#circle

img = cv2.circle(img, (447,63), 63, (0,255,0), 10)

#put text
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img,'THELEGEND', (-1,500), font, 3, (0, 0, 255), 10, cv2.LINE_AA)

cv2.imshow('dinesh', img)

cv2.waitKey(0)

cv2.destroyAllWindows()