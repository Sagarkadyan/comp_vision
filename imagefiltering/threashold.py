import cv2


images =cv2.imread("flower.png",cv2.IMREAD_GRAYSCALE)

ret, thres_img = cv2.threshold(images,120,225,cv2.THRESH_BINARY)

cv2.imshow("original image",images)
cv2.imshow("newimage",thres_img)
cv2.waitKey()
cv2.destroyAllWindows()
