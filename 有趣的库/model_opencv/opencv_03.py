# coding = utf-8
# 画线、长方形、圆等
import numpy as np
import cv2
# 返回一个数组
cv2.namedWindow('image')
img = np.zeros((512, 512, 3), np.uint8)
# 画线
cv2.imshow('image', img)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 画长方形
cv2.rectangle(img, (11, 11), (123, 123), (255, 0, 0), 3)
# 画圆
cv2.circle(img, (100, 100), 100, (255, 0, 0), -1)
# 画椭圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
# 向图片上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(2500)
