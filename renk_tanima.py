import cv2
import numpy as np


#camera = cv2.VideoCapture(0)
resim = cv2.imread("circles.jpg")

#while camera.isOpened():
   # _, frame = camera.read()


hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    
lower = np.array([0,100,100])
upper = np.array([10,255,255])
mask = cv2.inRange(hsv,lower,upper)
    #findcontours fonksiyonun içine binary resim verilmelidir.
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #çevre var.
"""
    contours: tespit edilen köşelerin ve bu tespit edilen köşelerin koordinatlarının tutulduğu liste oluşturur.
    hierarchy: child parent olayına benziyor.
    cv2.RETR_TREE:  hierarchy için kullanılır. Tüm konturları alır.
    RETR_EXTERNAL: sadece dış kontürleri çizdirmek istenirse bu kullanılabilir.
"""
for i, cnt in enumerate(contours): #cnt koordinat
    area = cv2.contourArea(cnt) #koordinatların oluşturduğu yerden alan hesabı yapılır.
    if area > 200:
        x,y,w,h = cv2.boundingRect(cnt) #alanın genişlik ve yüksekliklerini bulur.
        cv2.drawContours(resim, contours, i, (0,255,0), 3, cv2.LINE_8, hierarchy, 0) #i->counter id, içi dolu çizdirmek için kalınlık parametresi(3) -1 yapılır.
    
cv2.imshow("mask", mask)
cv2.imshow("resim", resim)

#if cv2.waitKey(5) == ord("q"):
#    break

cv2.waitKey()
cv2.destroyAllWindows()