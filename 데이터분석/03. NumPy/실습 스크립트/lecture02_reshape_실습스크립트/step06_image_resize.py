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

from PIL import Image # PIL(Python Image Lib) 


### 1. image resize
path = r"C:\ITWILL\5_Python_ML\workspace\chapter03_Numpy" # 이미지 경로 

# 1) image read 
img = Image.open(path + "/data/test1.jpg") 
np.shape(img) # 원본이미지 모양 

# 2) image resize 
img_re = img.resize( (150, 120) ) # (가로, 세로)
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)
plt.show()



### 2. 폴더 전체 이미지 resize 
from glob import glob # 파일 검색 패턴 사용(문자열 경로, * 사용) 


for file in glob(path + '/data/*.jpg'): # jpg 파일 검색    
    print(file) # jpg 파일 경로 












    
    
 


