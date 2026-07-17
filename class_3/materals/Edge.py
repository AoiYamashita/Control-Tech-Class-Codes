import cv2

image = cv2.imread("./hoge.png")

sobelx = cv2.Sobel(src=image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1)
sobely = cv2.Sobel(src=image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1)
sobelxy = cv2.Sobel(src=image, ddepth=cv2.CV_32F, dx=1, dy=1, ksize=1)

cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("sobelxy",sobelxy)

img_canny = cv2.Canny(image=image, threshold1=100, threshold2=200)

cv2.imshow("canny",img_canny)

cv2.waitKey(0)
