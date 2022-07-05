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

    return 'success'




# opt=  parse_opt()


# show_image('/Users/kyungmin/maze/y1/194.jpg',0,130,165,192,'/Users/kyungmin/maze/y1/area1.jpg')
# show_image('/Users/kyungmin/maze/y1/194.jpg',0,224,276,411,'/Users/kyungmin/maze/y1/area2.jpg')
# show_image('/Users/kyungmin/maze/y1/194.jpg',170,78,282,150,'/Users/kyungmin/maze/y1/area3.jpg')
# show_image('/Users/kyungmin/maze/y1/194.jpg',460,335,640,480,'/Users/kyungmin/maze/y1/area4.jpg')

show_image('/Users/kyungmin/maze/y1/194.jpg',0,130,165,192,'/Users/kyungmin/maze/y1/area.jpg')
show_image('/Users/kyungmin/maze/y1/area.jpg',0,224,276,411,'/Users/kyungmin/maze/y1/area.jpg')
show_image('/Users/kyungmin/maze/y1/area.jpg',170,78,282,150,'/Users/kyungmin/maze/y1/area.jpg')
show_image('/Users/kyungmin/maze/y1/area.jpg',460,335,640,480,'/Users/kyungmin/maze/y1/area.jpg')