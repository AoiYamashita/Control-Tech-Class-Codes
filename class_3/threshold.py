import cv2

image = cv2.imread("./hoge.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("th",th)

cv2.waitKey(0)

while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
