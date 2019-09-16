import cv2
img=cv2.imread("/home/dinesh/PycharmProjects/hello/messi5.jpg", 0)#imread class read img,channel
cv2.imshow(" leiono ", img)#imshow display image
k=cv2.waitKey(0) & 0xFF
if k==27:#ESC ASCII 27
   cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("theLegend.jpg", img)
    cv2.destroyAllWindows()