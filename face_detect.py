import cv2                   # pip install pencv-python

video = cv2.VideoCapture(1)

faces_base = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_alt2.xml')

while True:
       rat , frame = video.read(1)
       gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
       faces = faces_base.detectMultiScale(gray, scaleFactor=1.5  , minNeighbors=5)


       for (a,b,c,d) in faces:
            print(a,b,c,d)
            roi_gray = gray[b:b+d, a:a+c]
            image_test = 'image_test.png'
            cv2.imwrite(image_test , roi_gray)

            color  =  (255,0,0) #BGR
            strok = 2
            toul = a+c
            aerd = b+d
            cv2.rectangle(frame , (a,b) , (toul,aerd),color,strok)


       cv2.imshow('frame' , frame )
       if cv2.waitKey(20) & 0xff == (ord('q')):
           break


video.release()
cv2.destroyAllWindows()






