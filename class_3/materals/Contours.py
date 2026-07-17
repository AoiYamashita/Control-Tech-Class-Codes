import cv2


image = cv2.imread("./hoge_2.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 輪郭の検出
contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

im_con = image.copy()

im_con = cv2.drawContours(im_con, contours, -1, (0,255,0), 2)

for contour in contours:
    # 面積計算
    Area = cv2.contourArea(contour)
    # 重心計算
    moment = cv2.moments(contour)
    x = moment['m10']/moment['m00']
    y = moment['m01']/moment['m00']
    cv2.putText(im_con,f'{Area}', (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

    
cv2.imshow('result', im_con)
