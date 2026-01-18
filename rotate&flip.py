import cv2

image = cv2.imread("images.jpeg")
(h,w)=image.shape[:2]
#geting image diension
center = (w//2 , h//2)
#piont where from image will get rotated
zoom=1.0
angle=90
M = cv2.getRotationMatrix2D(center,angle,zoom)

rotated = cv2.warpAffine(image,M,(w,h))
#w,h refers to size of output image
cv2.imshow("rotated",rotated)



#fliping

flip_hor=cv2.flip(image,1)
flip_ver=cv2.flip(image,0)
flip_both=cv2.flip(image,-1)
cv2.imshow("horizontal",flip_hor)
cv2.imshow("vertical",flip_ver)
cv2.imshow("both",flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
