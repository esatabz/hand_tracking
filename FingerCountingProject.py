from email.mime import image
from sre_constants import SUCCESS
import cv2
import time
import os
import HandTrackingModule as htm   #手部追踪模块

wCam, hCam = 640, 480 #凸轮的宽度和相机的高度

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

#图像储存位置
folderPath = "/home/pi/Desktop/handtest1/pictures"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
#图像导入
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    print(f'{folderPath}/{imPath}')
    overlayList.append(image)  #列表追加，覆盖我们要添加的图像

print(len(overlayList))
pTime = 0

#检测器
detector = htm.handDetector(DetectionConfidnc = 0.75)

tipIds = [4, 8, 12, 16, 20]

while True:

    success,img = cap.read() #如果成功读取图像
    if not success:
        print("not:", img)
          # continue
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        fingers = []

        #damuzhi
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers

        if lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)


        if lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)


        if lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)


        if lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

        #totalFingers = fingers.count(1)
        print(fingers)

        #0
        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[10].shape
            img[0:h,0:w] = overlayList[10]
        #1
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[4].shape
            img[0:h,0:w] = overlayList[4]
        #2
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[5].shape
            img[0:h,0:w] = overlayList[5]
        #3
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            h,w,c = overlayList[6].shape
            img[0:h,0:w] = overlayList[6]
        #4
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            h,w,c = overlayList[9].shape
            img[0:h,0:w] = overlayList[9]
        #5
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            h,w,c = overlayList[13].shape
            img[0:h,0:w] = overlayList[13]
        #6
        if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            h,w,c = overlayList[7].shape
            img[0:h,0:w] = overlayList[7]
        #7
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            h,w,c = overlayList[12].shape
            img[0:h,0:w] = overlayList[12]
        #8
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[0].shape
            img[0:h,0:w] = overlayList[0]
        #9
        if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[2].shape
            img[0:h,0:w] = overlayList[2]
        #shang
        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[11].shape
            img[0:h,0:w] = overlayList[11]
        #xia
        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            h,w,c = overlayList[8].shape
            img[0:h,0:w] = overlayList[8]
        #aixin
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            h,w,c = overlayList[1].shape
            img[0:h,0:w] = overlayList[1]
        #ok
        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            h,w,c = overlayList[3].shape
            img[0:h,0:w] = overlayList[3]


        #h,w,c = overlayList[0].shape
        #img[0:h,0:w] = overlayList[0]  #高度与宽度限制（基于图片尺寸大小可以更改）  现在固定在了角落

        #cv2.rectangle(img, (20,225), (170,425), (0, 255, 0), cv2.FILLED)
        #cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    #显示帧率
    #cTime = time.time()
    #fps = 1 / (cTime-pTime)
    #cv2.putText(img,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,
    #            3,(255,0,0),3)   #   颜色，厚度

    cv2.imshow("Image",img)
    cv2.waitKey(1)