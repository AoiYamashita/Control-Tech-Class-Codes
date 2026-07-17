import cv2

cap = cv2.VideoCapture(0)

while True:
   # フレームを取得
   ret, frame = cap.read()
   if not ret:
       print("カメラから映像が取得できませんでした")
       break
   # 映像をウィンドウに表示
   cv2.imshow("Camera", frame)
   if cv2.waitKey(1) == 27:
       break

cap.release()
cv2.destroyAllWindows()