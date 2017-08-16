import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_cascade=cv2.CascadeClassifier("eye.xml")
imge=cv2.imread("exep.jpg")
#imge_gray=cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(imge,
scaleFactor=1.05,
minNeighbors=15)
print(faces)
for i in faces.flat:
      print(i)
for x,y,w,h in faces:
        img=cv2.rectangle(imge,(x,y),(x+w,y+h),(0,255,0),3)
font=cv2.FONT_HERSHEY_COMPLEX
list=[305,233,197,197]

if not any(i in list for i in faces.flat):
            cv2.putText(imge,"detail error!!", (200,600), font, 1, (0,0,0))
else:
     cv2.putText(imge,"Hello World!!!", (250,600), font, 1, (0,0,0))
cv2.imshow("gray",imge)

cv2.waitKey(7000)
cv2.destroyAllWindows()
