import cv2
import os
from time import strftime


cap = cv2.VideoCapture(0)
count = 0
while cap.isOpened():
    tm = strftime('%H:%M:%S')
    _, frame = cap.read()

    save_path = os.getcwd()+f'/pictures/{count}.jpg'
    while os.path.exists(save_path):
        count += 1
        save_path = os.getcwd()+f'/pictures/{count}.jpg'
    cv2.imwrite(save_path,frame)
    count+=1
    if count>20:
            break

cap.release()

