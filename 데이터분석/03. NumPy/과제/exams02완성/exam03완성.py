'''
문3) 다음과 같이  단계별로 자료구조를 생성하시오.
    단계1 : 1~84 정수를  이용하여 벡터 생성
    단계2 : 벡터를 대상으로 7x3x4 구조의 3차원 배열로 모양 변경
    단계3 : 3차원 배열을 대상으로 (행,면,열) 축의 순서로 구조 변경
'''

import numpy as np

# 1. vector 생성 : list -> np.array(list)
lst = list(range(1, 85)) # list 객체 
arr1d = np.array(lst) # numpy array 
arr1d.shape # (84,)

# 2. 3차원 배열 
arr3d = arr1d.reshape(7,3,4)
arr3d.shape # (7, 3, 4)
arr3d

# 3. transpose(행,면,열)
arr3d_tran = arr3d.transpose(1, 0, 2) # 면 <-> 행 
arr3d_tran.shape # (3, 7, 4)
arr3d_tran

