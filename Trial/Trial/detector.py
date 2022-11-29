import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while 1:
    ret,frame =cap.read()
    convert_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   
    Lower_limit=np.array([0,100,100]) 
    Upper_limit=np.array([20,255,255])
        
 
    r_mask=cv2.inRange(convert_hsv,Lower_limit,Upper_limit)
  
    red=cv2.bitwise_and(frame,frame,mask=r_mask)
    cv2.imshow('Original',frame) 
    cv2.imshow('Red Detector',red) 
 
    if cv2.waitKey(1)==13:
        break
   
cap.release()
 
cv2.destroyAllWindows()