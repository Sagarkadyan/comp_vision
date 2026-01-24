import cv2
img = cv2.imread("images.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

contours , heirarchy  =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),5)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corners=len(approx)
    if corners ==3:
        shape_name="triangle"
    elif corners ==4:
        shape_name="rectangle"
    elif corners ==5:
        shape_name="pentagon"
    elif corners >5:
        shape_name="circle"    
    else :
        shape_name ="unknown"    

    cv2.drawContours(img,[approx],0,(0,255,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0))

cv2.imshow("original image",img)
cv2.waitKey()
cv2.destroyAllWindows()