import cv2
import numpy as np


resim = cv2.imread("renk_tanima\circles.jpg")

hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    
lower = np.array([0,100,100])
upper = np.array([10,255,255])
mask = cv2.inRange(hsv,lower,upper)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for i, cnt in enumerate(contours): 
    area = cv2.contourArea(cnt) 
    if area > 200:
        x,y,w,h = cv2.boundingRect(cnt) 
        cv2.drawContours(resim, contours, i, (0,255,0), 3, cv2.LINE_8, hierarchy, 0) 
    
cv2.imshow("mask", mask)
cv2.imshow("resim", resim)

cv2.waitKey()
cv2.destroyAllWindows()
