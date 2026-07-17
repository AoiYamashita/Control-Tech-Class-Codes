import cv2
import numpy as np

image = cv2.imread("./openCV.png")

red = image[:,:,2]
green = image[:,:,1]
blue = image[:,:,0]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval, bw = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# 輪郭の検出
contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

text_contour = []
for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    Area = cv2.contourArea(contour)
    Rave = np.average(red[int(y-radius):int(y+radius),int(x-radius):int(x+radius)])
    Gave = np.average(green[int(y-radius):int(y+radius),int(x-radius):int(x+radius)])
    Bave = np.average(blue[int(y-radius):int(y+radius),int(x-radius):int(x+radius)])

    if Rave/255 > 0.9:
        image = cv2.circle(image, center, radius, (255, 0, 0), 2)
    elif Gave/255 > 0.9:
        image = cv2.circle(image, center, radius, (0, 0 ,255), 2)
    elif Bave/255 > 0.9:
        image = cv2.circle(image, center, radius, (0, 255, 0), 2)
    else:
        text_contour.extend(contour)

rect = cv2.minAreaRect(np.array(text_contour))
box = cv2.boxPoints(rect)
box = np.int32(box)
image = cv2.drawContours(image, [box], -1, (0, 200,200), 2)

cv2.imshow('result', image)

while True:
    key = cv2.waitKey(25)

    if key == ord('q'):
        cv2.destroyAllWindows()
        break