# coding = utf-8
# 书籍：<<学习opencv>>
import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("girl.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imwrite("girl.png", img)
# cv2.imshow("image", img)
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# k = cv2.waitKey()
# if k == 27:
#    cv2.destroyAllWindows()
# elif k == ord('s'):
#    cv2.imwrite("girl.bmp", img)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
plt.show()