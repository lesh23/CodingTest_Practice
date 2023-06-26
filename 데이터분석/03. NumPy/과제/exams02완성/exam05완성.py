'''
문5) 다음 같은 가중치(weight)와 입력(X)를 이용하여 히든 노드(hidden node)를 구하시오.      
    <단계1> weight(3,3) 행렬 만들기 : 표준정규분포 난수 자료 이용   
    <단계2> X(3,1) 행렬 만들기 : 1,2,3 자료 이용      
    <단계3> weight행렬과  X행렬 대상으로 행렬곱 연산   
           계산식 : hidden(3,1) = weight(3,3) @ X(3,1)   
'''

import numpy as np

print('단계1 : weight 행렬 만들기')
weight = np.random.randn(3,3)
weight
'''
array([[ 0.53570289, -0.90170057,  0.24804147],
       [ 1.23161317, -0.38188971,  0.43710766],
       [-2.03234124, -1.86495032,  0.41355889]])
'''
weight.shape # (3, 3)

print('단계2 : X 행렬 만들기')
X = np.array([[1],[2],[3]])
X.shape # (3, 1)

print('단계3 : hidden node 계산')
hidden_node = weight.dot(X) # weight @ X
hidden_node
'''
[[-0.52357382],
 [ 1.77915672],
 [-4.5215652 ]]
'''
hidden_node.shape # (3, 1)

