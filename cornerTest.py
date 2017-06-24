import numpy as np
import cv2

img = cv2.imread('testm.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 11)
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),1,255,-1)
    
cv2.imshow('Corner',img)
cv2.waitKey()
cv2.destroyAllWindows()
