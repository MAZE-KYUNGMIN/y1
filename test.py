import cv2
from time import strftime
from time import time
import timeit

s = int(strftime('%S'))
prev_time = 0 
count = 0 
cap  = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()

    t1 = time() # 시작 시각

    if ret and count >= 0 and 50 > count :
        # print(f'prop fps : {cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)}')
        # print(f'prop fps : {cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)}')
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        cv2.imshow('frame',frame)
        print(f'첫번째')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    if ret and count >= 50 and 100 > count:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cv2.imshow('frame',frame)
        # print(f'prop fps : {cap.get(cv2.CAP_PROP_FPS)}')
        print(f'두번째')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if ret and count >= 100:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
        cv2.imshow('frame',frame)
        # print(f'prop fps : {cap.get(cv2.CAP_PROP_FPS)}')
        print(f'세번째')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    if count > 150:
        count = 0
        print('사이클 완료')
    
    t2 = time() # 끝낸 시각
    fps = round(1./(t2 - t1))
    print(f'fps : {fps}')
    count += 1

cap.release()
