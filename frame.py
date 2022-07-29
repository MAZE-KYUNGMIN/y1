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

    if ret and count == 1:
        cv2.imshow('frame',frame)
        print('첫번째')


    if ret and count == 2:
        cv2.imshow('frame',frame)
        print('두번째')
        break
    
    count +=1

    t2 = time() # 끝낸 시각
    fps = 1./(t2 - t1)
    print(f'fps : {fps}')

    if cv2.waitKey(1000) > 0:
        break


cap.release()

