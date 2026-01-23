import cv2

image = cv2.imread("images.jpeg")
pt1 =(100,50)
pt2=(200,300)
colour=(255,0,0)
thickness=3
line_img=cv2.line(image,pt1,pt2,colour,thickness)
cv2.imshow("line",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("lineonimage.jpeg",line_img)
