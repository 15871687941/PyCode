# coding = utf-8
import numpy as np
import cv2
import random

img = cv2.imread('girl.jpg')
cv2.namedWindow('image')
# for x in range(0, img.shape[0]):
    # for y in range(0, img.shape[1]):
        # img.itemset((x, y), [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
# print(type(img))
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# b, g, r = cv2.split(img)
# print(b, g, r)
# img = cv2.merge((b, g, r))
print(img.item(100, 100, 2))
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey()
