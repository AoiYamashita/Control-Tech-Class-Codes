import cv2

image = cv2.imread("./hoge.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("th",th)

import numpy as np

ex_img = np.zeros(image.shape,dtype=np.uint8)

ex_img[th == 255] = image[th == 255]

cv2.imshow("hoge",ex_img)
