# coding = utf-8
import numpy as np
import cv2


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x-50, y-50), (x+50, y+50), (0, 255, 0), -1)
    else:
        pass


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(10) == ord('q'):
        break;
cv2.destroyAllWindows()