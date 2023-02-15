import cv2 
import os

os.chdir('C:\\Users\\mina1\\source\\Python_files\\Test2023_data')

frontalFaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
profileFaceCascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

#img = cv2.imread('yosry1.jpg',0)
capture = cv2.VideoCapture('yosryV.mp4')
cv2.waitKey(0)

while capture.isOpened():
    ret, img = capture.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    frontalFaces = frontalFaceCascade.detectMultiScale(gray,1.1,4)
    #profileFaces = profileFaceCascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in frontalFaces:
        if w > 100 or h > 100:
	        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    #for (x,y,w,h) in profileFaces:
        #if w > 100 or h > 100:
	        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("image", img)
    if cv2.waitKey(1) == ord('q'):
            break 

capture.release()
cv2.destroyAllWindows()