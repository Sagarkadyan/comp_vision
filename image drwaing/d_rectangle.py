import cv2

image = cv2.imread("images.jpeg")
pt1 =(100,50)
pt2=(150,130)
#here pt1 & pt2 are the top and bottom opposite corner
colour=(55,13,31)
thickness=3
rectangle=cv2.rectangle(image,pt1,pt2,colour,thickness)
cv2.imshow("rectangle",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rectangleonimage.jpeg",rectangle)
