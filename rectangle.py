import cv2
import numpy
import os
import argparse

red_color = (0,0,255)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x1',type=int, default=0)
    parser.add_argument('--x2',type=int, default=0)
    parser.add_argument('--y1',type=int, default=0)
    parser.add_argument('--y2',type=int, default=0)

    opt = parser.parse_args()

    return opt


def show_image(img_path,x1,y1,x2,y2,save_path):
    img = cv2.imread(img_path)
    cv2.rectangle(img,(x1,y1),(x2,y2),red_color,2)
    cv2.imwrite(save_path,img)

    return print('success')




# opt=  parse_opt()


# show_image('/Users/kyungmin/maze/y1/1655.jpg',252,194,362,292,'/Users/kyungmin/maze/y1/area1.jpg')
# show_image('/Users/kyungmin/maze/y1/1655.jpg',0,160,106,215,'/Users/kyungmin/maze/y1/area2.jpg')
# show_image('/Users/kyungmin/maze/y1/1655.jpg',91,91,206,154,'/Users/kyungmin/maze/y1/area3.jpg')
# show_image('/Users/kyungmin/maze/y1/1655.jpg',0,258,240,430,'/Users/kyungmin/maze/y1/area4.jpg')
# show_image('/Users/kyungmin/maze/y1/1655.jpg',404,323,640,480,'/Users/kyungmin/maze/y1/area5.jpg')
# show_image('/Users/kyungmin/maze/y1/1655.jpg',538,228,640,305,'/Users/kyungmin/maze/y1/area6.jpg')


# show_image('/Users/kyungmin/maze/y1/1655.jpg',252,194,362,292,'/Users/kyungmin/maze/y1/all_area.jpg')
# show_image('/Users/kyungmin/maze/y1/all_area.jpg',0,160,106,215,'/Users/kyungmin/maze/y1/all_area.jpg')
# show_image('/Users/kyungmin/maze/y1/all_area.jpg',91,91,206,154,'/Users/kyungmin/maze/y1/all_area.jpg')
# show_image('/Users/kyungmin/maze/y1/all_area.jpg',0,258,240,430,'/Users/kyungmin/maze/y1/all_area.jpg')
# show_image('/Users/kyungmin/maze/y1/all_area.jpg',404,323,640,480,'/Users/kyungmin/maze/y1/all_area.jpg')
# show_image('/Users/kyungmin/maze/y1/all_area.jpg',538,228,640,305,'/Users/kyungmin/maze/y1/all_area.jpg')