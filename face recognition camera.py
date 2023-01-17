import cv2
import numpy as np
import keyboard

cv2.namedWindow("Cam preview")
cv2.namedWindow("S1")
vc = cv2.VideoCapture(0)
FaceCascade = cv2.CascadeClassifier(r"C:\Users\5\Downloads\haarcascade_frontalface_default.xml")



if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    flipHorizontal = cv2.flip(frame, 1)
    faces = FaceCascade.detectMultiScale(flipHorizontal, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(flipHorizontal, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow("Cam preview", flipHorizontal)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27:
            break

vc.release()
cv2.destroyWindow("Cam preview")