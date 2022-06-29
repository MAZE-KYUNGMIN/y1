import cv2
import os
from time import strftime


cap = cv2.VideoCapture(0)
count = 0
while cap.isOpened():
    tm = strftime('%H:%M:%S')
    _, frame = cap.read()

    save_path = os.getcwd()+f'/{count}.jpg'

    cv2.imwrite(save_path,frame)
    print(tm)
    count+=1
    if count>10:
            break

cap.release()

