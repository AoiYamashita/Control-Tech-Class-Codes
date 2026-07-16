import cv2

image = cv2.imread("./hoge.png")

print(f"image shape : {image.shape}")

print(f"image data : {image}")

cv2.imshow("hoge",image)

cv2.waitKey(0)