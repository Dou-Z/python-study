# # -*- coding:utf-8 -*-

import cv2

impath = "0.jpg"
image = cv2.imread('0.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
fa = face_cade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5)
for (x, y, w, h) in fa:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255.0), 2)
cv2.imwrite('cv_final.jpg', image)