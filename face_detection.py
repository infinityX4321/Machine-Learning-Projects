import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("C:\\Users\\pc\\Downloads\\New folder\\Video1.mp4",0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
myFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)
drawSpec = myDraw.DrawingSpec(thickness=1,circle_radius=1)
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mp.Draw.draw_landsmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS,drawSpec,drawSpec)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows
