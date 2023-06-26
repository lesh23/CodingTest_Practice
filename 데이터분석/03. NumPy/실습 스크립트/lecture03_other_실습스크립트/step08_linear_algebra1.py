# -*- coding: utf-8 -*-
"""
 선형대수 관련 함수 
  - 수학의 한 분야 
  - 벡터 또는 행렬을 대상으로 한 연산
"""

import numpy as np 

# 1. 선형대수 관련 함수
 
# 1) 단위행렬 : 대각원소가 1이고, 나머지는 모두 0인 n차 정방행렬
eye_mat = np.eye(3) 
print(eye_mat)


# 정방행렬 x
x = np.arange(1,10).reshape(3,3)
print(x)


# 2) 대각성분 추출 
diag_vec = np.diag(x)
print(diag_vec) # 대각성분 : [1 5 9]


# 3) 대각합 : 정방행렬의 대각에 위치한 원소들의 합 
trace_scala = np.trace(x) # 
print(trace_scala)


# 4) 대각행렬 : 대각성분 이외의 모든 성분이 모두 '0'인 n차 정방행렬
diag_mat = eye_mat * diag_vec
print(diag_mat)


# 5) 행렬식(determinant) : 대각원소의 곱과 차 연산으로 scala 반환 
x = np.array([[3,4], [1,2]])
print(x)

det = np.linalg.det(x)
print(det) 


# 6) 역행렬 : 행렬식의 역수를 정방행렬 대응 곱셈 
inv_mat = np.linalg.inv(x)
print(inv_mat)





