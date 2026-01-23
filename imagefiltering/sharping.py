import cv2
import numpy as np

images = cv2.imread("low_res.jpeg")

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpen = cv2.filter2D(images,-10,sharpen_kernel)
cv2.imshow("sharepen image",sharpen)
cv2.imshow("original image",images)
cv2.waitKey()
cv2.destroyAllWindows()