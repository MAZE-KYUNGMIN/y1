from glob import glob
import os
from pathlib import Path
import cv2

def len_path(path):
    x = len(glob(f'{path}/*'))
    return x



def match(images,labels):
    images = os.listdir(images)
    labels = os.listdir(labels)
    count = 0
    for i in images:
        j = i[:-3] + 'txt'
        if j not in labels:
            path = os.path.join(os.getcwd(),'preprocessing/images/'+i)
            print(os.path.exists(path))
            if os.path.exists(path):
                os.remove(path)
        else:
            pass
    return 's'

    
def split_image(lst,path):
    for i,img in enumerate(lst):
        img = cv2.imread(img)
        image_path = path + f'/{str(i)}.jpg'
        cv2.imwrite(image_path,img)


def split_label(lst,save_path):

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
        
    for i,lbl in enumerate(lst):
        with open(lbl,'r',encoding='utf-16') as f:
            lines = f.readlines()
        with open(save_path+f'/{str(i)}.txt','w') as f:
            f.write(lines)




images=  'preprocessing/images/'
labels = 'preprocessing/labels/'
match(images,labels)

# BASE_PATH = '.'
# BASE_PATH = os.path.abspath(BASE_PATH)


# img_path = '/Users/kyungmin/lucida/images'
# lbl_path = '/Users/kyungmin/lucida/labels'

# match(img_path,lbl_path)

# images = glob(f'{img_path}/*')
# labels = glob(f'{lbl_path}/*')

# print(images == labels)

# print(len_path(img_path))

