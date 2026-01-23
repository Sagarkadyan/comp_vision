import cv2

# images = cv2.imread("flower.png")
# images =cv2.imread("flower.png",cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(images,50,150)

cv2.imshow("original image",images)
cv2.imshow("newimage",edges)
cv2.waitKey()
cv2.destroyAllWindows()