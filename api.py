from distutils.command.upload import upload
import sys
import json
import requests
import os
import glob

url = 'http://localhost:3004/upload-multi'
lst = glob.glob('/Users/kyungmin/study/images/*.jpg')
files = []
close = []
count=0
for i in lst:
    files.append(('files',(f'{i}',open(i,'rb') ,'uploads')))
    close.append(open(i,'rb'))
        

response = requests.post(url, files=files)
for i in close:
    i.close()

