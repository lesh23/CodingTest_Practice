# -*- coding: utf-8 -*-
"""
step06_image_resize.py

image resize
   reshape vs resize 
   reshape : 모양 변경(size 변경 불가)
   resize :  size 변경 -> 모양 변경
"""

import numpy as np 
import matplotlib.pyplot as plt # image show 

from PIL import Image # PIL(Python Image Lib) : 읽기, 크기변경 


### 1. image resize
path = r"C:\ITWILL\5_Python_ML\workspace\chapter03_Numpy" # 이미지 경로 

# 1) image read 
img = Image.open(path + "/data/test1.jpg") 
type(img) # PIL.JpegImagePlugin.JpegImageFile
#img.shape 

plt.imshow(img)
plt.show()

np.shape(img) # 원본이미지 모양 
#  (360, 540, 3) : (세로, 가로, 칼럼) - (120, 150)

# 2) image resize 
img_re = img.resize( (150, 120) ) # (가로, 세로)
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)
plt.show()


### 2. 폴더 전체 이미지 resize 
from glob import glob # 파일 검색 패턴 사용(문자열 경로, * 사용) 
'''
dir *.txt
dir ??.txt
'''

img_resize = [] # 이미지 크기 변경 
img_w = 150; img_h = 120 # 이미지 가로/세로 

for file in glob(path + '/data/*.jpg'): # jpg 파일 검색    
    #print(file) # jpg 파일 경로 
    img = Image.open(file) # 1) image 읽기 : PIL 객체 
    
    img = img.resize( (img_w, img_h) ) # 2) 크기변경 : (150, 120) 
    
    # 3) PIL -> numpy -> list 저장  
    img_resize.append(np.array(img))
    
    
# resize 이미지 확인 
img_arr = np.array(img_resize) # list -> np.array 
img_arr.shape # (4, 120, 150, 3) : (size, h, w, c)

img_arr[0].max() # 0 ~ 255(R,G,B)

first_img = img_arr[0]
first_img.shape # (120, 150, 3)
first_img[:,:,0] # R
first_img[:,:,1] # G
first_img[:,:,2] # B

# image 확인 
for i in range(len(img_arr)) :
    print(img_arr[i].shape)
    plt.imshow(img_arr[i]) # i=0~n-1
    plt.show()

    
    
 


