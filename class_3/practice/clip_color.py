import cv2
import numpy as np

image = cv2.imread("./openCV.png")

red = image[:,:,2]
green = image[:,:,1]
blue = image[:,:,0]
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, red_th = cv2.threshold(red, 0, 255, cv2.THRESH_OTSU)
ret, green_th = cv2.threshold(green, 0, 255, cv2.THRESH_OTSU)
ret, blue_th = cv2.threshold(blue, 0, 255, cv2.THRESH_OTSU)
ret, black_th = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

red_only = image.copy()
red_only[red_th == 0] = np.array([255]*3)
red_only = cv2.medianBlur(red_only,5)

green_only = image.copy()
green_only[green_th == 0] = np.array([255]*3)
green_only = cv2.medianBlur(green_only,5)

blue_only = image.copy()
blue_only[blue_th == 0] = np.array([255]*3)
blue_only = cv2.medianBlur(blue_only,5)

cv2.imshow("red",red_only)
cv2.imshow("green",green_only)
cv2.imshow("blue",blue_only)
cv2.imshow("black",black_th)

cv2.waitKey(0)
