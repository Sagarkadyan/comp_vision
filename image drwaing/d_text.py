import cv2

image = cv2.imread("images.jpeg")
text="what's up "
org=(50,25)
#org is the bottom left coordinate of text or starting poit of text
font=cv2.FONT_HERSHEY_DUPLEX
fontscale=1.2
color=(13,45,164)
thickness=3

text_img=cv2.putText(image,text,org,font,fontscale,color,thickness)
cv2.imshow("text",text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("textedonimage.jpeg",text_img)
