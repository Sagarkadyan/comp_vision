import cv2

images = cv2.imread("blur.jpeg")

blurred = cv2.medianBlur(images,5)

cv2.imshow("original",images)
cv2.imshow("blur",blurred)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("median_clean.jpeg",blurred)