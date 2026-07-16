import cv2

image = cv2.imread("./hoge.png")

cv2.imshow("Red",image[:,:,2])
cv2.imshow("Green",image[:,:,1])
cv2.imshow("Blue",image[:,:,0])

cv2.waitKey(0)
