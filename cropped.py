import cv2

image = cv2.imread("images.jpeg")

cv2.imshow("original image",image)

cropped =image[10:180,20:200]
#10=starting y axis 180 is ending y axis 20 is starting x axis and 200 is ending x anis
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("cropped image",cropped)
