''' Chap 3. 내장자료구조, 함수, 파일 '''

### 튜플 : *rest -> rest가 자료 이름
tu = 1,2,4,5,8
a,b,*c = tu
# a =1, b=2, c=[4,5,8]

### 리스트
li = [1,2,3,4]
li.insert(0, -1) # 0번 인덱스에 값 -1 추가
li # [-1, 1, 2, 3, 4]

li.pop(0) # 0번 인덱스의 값 삭제 [1,2,3,4]
li.remove(3) # 값 제거, 중복 값 있을시 맨 앞에 위치한 값 삭제 [1,2,4] 
li.extend(['a','b']) # 리스트 이어붙이기, + 연산자로도 가능
li # [1, 2, 4, 'a', 'b']

# 리스트 정렬
a = [2,61,84,1,5,3,6,544]
a.sort() # 새로운 리스트 생성없이 그대로 리스트 정렬

b = ['a', 'apple', 'banana', 'cat', 'watermelon']
b.sort(key = len) # 리스트를 문자열의 길이 순으로 정렬 가능
b # ['a', 'cat', 'apple', 'banana', 'watermelon']


### bisect : 정렬된 배열에서 이진탐색
import bisect
a = [1,2,2,3,4,5,8]



# Numpy

import numpy as np

arr = np.arange(1000)
arr






''' Chap 5. pandas 시작하기 '''
import pandas as pd

# 184p
sdata = {'Ohio' : 35000, 'Texas':71000, 'Oregon':16000,'Utah' : 5000}
obj3 = pd.Series(sdata)
obj3
states = ['California', 'Ohio','Oregon','Texas']
obj4 = pd.Series(sdata, index = states)
obj4

# 193p
pop = {'Nevada' : {2001 : 2.4, 2002:2.9},
       'Ohio' : {2000:1.5, 2001:1.7, 2002:3.6}}

frame3 = pd.DataFrame(pop)
frame3

frame3.T
pd.DataFrame(pop, index = [2001,2002,2003])






















