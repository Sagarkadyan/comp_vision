import cv2
#how to load image
image = cv2.imread("images.jpeg")
#how to show image
cv2.imshow("NORMAL CAT",image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#image gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale CAT",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


resize = cv2.resize(image,(100,100))
#first witdh and height
cv2.imshow("resized cat",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("rezize cat.png",resize)
#to save the image




