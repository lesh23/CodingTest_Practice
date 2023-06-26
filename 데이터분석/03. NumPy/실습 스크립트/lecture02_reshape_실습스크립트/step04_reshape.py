# -*- coding: utf-8 -*-
"""
reshape : 모양 변경 
 - 1차원 -> 2차원 
 - 2차원 -> 다른 형태의 2차원  
T : 전치행렬 
swapaxis : 축 변경 
transpose : 축 번호 순서로 구조 변경 
"""

import numpy as np

# 1. 모양변경
lst = list(range(1, 13)) # 1차원 배열
 
arr2d = np.array(lst).reshape(3, 4) # 모양변경
print(arr2d)

# 2. 전치행렬
print(arr2d.T)
print(arr2d.T.shape) # (4, 3)

# 3. swapaxes : 축 변경 
print('swapaxes')
print(arr2d.swapaxes(0, 1)) 

# 4. transpose
'''
3차원 : 축 순서를 이용하여 자료 구조 변경 
'''
arr3d = np.arange(1, 25).reshape(4, 2, 3)#(4면2행3열)
#print(arr3d)
print(arr3d.shape) 

# default : (면,행,열) -> (열,행,면)
arr3d_def = arr3d.transpose() # 파리미터 없음
print(arr3d_def.shape) 
print(arr3d_def)
