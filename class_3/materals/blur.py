import cv2

image = cv2.imread("./hoge.png")

img_blur = cv2.blur(src=image, ksize=(5, 5))

cv2.imshow("blur",img_blur)

img_gauss = cv2.GaussianBlur(image, (3, 3), sigmaX=3)

cv2.imshow("gauss",img_gauss)

img_median = cv2.medianBlur(src=image, ksize=3)

cv2.imshow("median",img_median)

cv2.waitKey(0)
