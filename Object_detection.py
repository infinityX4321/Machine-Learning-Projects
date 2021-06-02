import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)#to capture video using webcam and 0 for binarry image
ret,frame = cap.read() # capture the frame
frame =cv2.flip(frame,+1) # moirror the image
frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#for hue,saturation and view
lb = np.array([153,119,212]) #upper thresold
ub = np.array([255,255,255]) #lower thresold
mask = cv2.inRange(frame2,lb,ub) #remove other values and takes values between lb and ub
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#morphology is used to remove the noise present in the image
#kernel stands for umity matrix
res = cv2.bitwise_and(frame,frame2,mask=opening)# adddion of two image
contours,hierarchy = cv2.findContours(opening,cv2.RETR_TREE,
                                      cv2.CHAIN_APPROX_NONE)
if len(contours)!= 0:
    cnt = contours[0]
    M = cv2.moments(cnt)
    Cx = int(M['m10']/M['m00'])
    Cy = int(M['m01']/M['m00'])
    S = 'Location of object:'+'('+str(Cx)+',' + str(Cy)+')'
    cv2.putText(frame,S,(5,50),font,2,ArithmeticError(0,0,255),2, cv2.LINE_AA)
    cv2.drawContours(frame,cnt,-1,(0,255,0),3)
cv2.imshow("Original Image",frame)
#cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
