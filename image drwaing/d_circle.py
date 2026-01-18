import cv2

image = cv2.imread("images.jpeg")
center=(136,82)
radius=50
#here pt1 & pt2 are the top and bottom opposite corner
colour=(55,123,241)
thickness=5
#if value of thickness is negative then the circle will be filled completly else it will be an outline
circle=cv2.circle(image,center,radius,colour,thickness)
cv2.imshow("circle",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("circleonimage.jpeg",circle)
