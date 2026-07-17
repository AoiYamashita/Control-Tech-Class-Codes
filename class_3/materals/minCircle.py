import cv2
import numpy as np

image = cv2.imread("./hoge_2.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 輪郭の検出
contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    image = cv2.circle(image, center, radius, (0, 255, 0), 2)

cv2.imshow('result', image)

while True:
    key = cv2.waitKey(25)

    if key == ord('q'):
        cv2.destroyAllWindows()
        break