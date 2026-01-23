import cv2

images = cv2.imread("images.jpeg")

blurred = cv2.GaussianBlur(images,(3,3),0)
cv2.imshow("blurred image",blurred)
cv2.imshow("original image",images)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("gussian_clean.jpeg",blurred)