import cv2

img=cv2.imread("/home/dinesh/Desktop/Tom-and-Jerry-768x404.jpg",1)

resize=cv2.resize(img,(int (img.shape[1]*2),int (img.shape[0]*2)))

cv2.imshow("Myphoto",resize)

cv2.waitKey(2000)

cv2.destroyAllWindows()