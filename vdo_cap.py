import cv2,time

video=cv2.VideoCapture(0)

check,frame=video.read()

print(check)
print(frame)

cv2.imshow("Dinesh",frame)

cv2.waitKey()

time.sleep(3)

video.release()

cv2.destroyAllWindows()
