# coding = utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cv2.namedWindow('image')
while cap.isOpened():
    res, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('image', hsv)
    if cv2.waitKey(25) == ord('q'):
        break
# cv2.destroyAllWindows()
