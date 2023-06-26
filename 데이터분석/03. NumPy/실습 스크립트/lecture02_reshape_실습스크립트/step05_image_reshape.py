# -*- coding: utf-8 -*-
"""
step05_image_reshape.py

1. image shape & reshape 
2. image file read & show
"""

import matplotlib.pyplot as plt  
from sklearn.datasets import load_digits 


# 1. image shape & reshape

# 1) dataset load 
digits = load_digits() # 머신러닝 모델에서 사용되는 데이터셋 
'''
입력변수(X) : 숫자(0~9) 필기체의 흑백 이미지 
출력변수(y) : 10진 정수
'''
X = digits.data # 입력변수(X) 추출 
y = digits.target # 출력변수(y) 추출 

# 2) image reshape 
first_img = X[0].reshape(8,8) # 모양변경 
first_img.shape # (8, 8)


# 3) image show 
plt.imshow(X=first_img, cmap='gray')
plt.show()


# 2. image file read & show
import matplotlib.image as img # 이미지 읽기 

# image file path 
path = r"C:\ITWILL\5_Python_ML\workspace\chap03_Numpy" # 이미지 경로 

# 1) image 읽기 
img_arr = img.imread(path + "/images/test1.jpg")
img_arr

# 2) image 출력 
plt.imshow(img_arr)
plt.show()

