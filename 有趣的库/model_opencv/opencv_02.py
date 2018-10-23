# coding = utf-8
# Getting Started with Videos
import cv2
import numpy as np

cap = cv2.VideoCapture('偶像宣言(第001集)[流畅].mp4')
# if you want to save it, must do these
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    # gray = cv2.flip(gray, 0)
    cv2.imshow('frame', frame)
    # out.write(gray)
    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
