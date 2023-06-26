# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징 
 - pandas 1차원(vector) 자료구조 
 - DataFrame의 칼럼 구성요소 
 - 수학/통계 관련 함수 제공 
 - indexing/slicing 기능 : list 유사함  
"""

import pandas as pd # 별칭  
from pandas import Series # class 
'''
pd.Series() # 별칭 이용 
Series() # class 이용 
'''

# 1. Series 객체 생성 

# 1) list 이용 
price = pd.Series([3000,2000,1000,5200]) # list 이용 
print(price) # 숫자기반 색인 
'''
0    3000
1    2000
2    1000
3    5200
dtype: int64 -> 자료형(통일)
'''
type(price) # pandas.core.series.Series
dir(price) # 호출가능한 메서드(), 속성(index, values)  

idx = price.index
values = price.values
idx #  RangeIndex(start=0, stop=4, step=1)
values # array([3000, 2000, 1000, 5200], dtype=int64)

# 색인 참조 
price[1] #  2000


# 2) dict 이용 : {key:value} -> (index, values)
person = Series({'name':'홍길동', 'age':35, 'addr':'서울시'}) 
print(person) # 명칭(문자)기반 색인 
'''
name    홍길동
age      35
addr    서울시
dtype: object -> 자료형(통일) 
'''
person['addr'] # '서울시'


# 2. indexing/slicing : list 동일 
ser = Series([4, 4.5, 6, 8, 10.5])  
print(ser)
len(ser) # 5 

ser[:] # 전체 원소[start:step] 
ser[0] # 1번 원소 
ser[:3] # start~2번 원소 
ser[3:] # 3~end 원소 
#ser[-1] # 사용불가 

ser2 = ser[:3] # new object 
ser2


# 3. Series 결합과 NA 처리 
s1 = pd.Series([3000, None, 2500, 2000],
               index = ['a', 'b', 'c', 'd'])

s2 = pd.Series([4000, 2000, 3000, 1500],
               index = ['a', 'c', 'b', 'd'])

s1
s2

# Series 결합(사칙연산)
s3 = s1 + s2
print(s3)
'''
a    7000.0
b       NaN  -> 결측치 
c    4500.0
d    3500.0
'''

dir(s3)


# 결측치 처리 : 통계 or 상수 대체, 제거 
result = s3.fillna(s3.mean()) # 평균 채우기 
print(result)

result2 = s3.fillna(0) # 0 채우기 
print(result2)


# 결측치 제거 
pd.notnull(s3) # True or False 

result3 = s3[pd.notnull(s3)] # 조건색인 
print(result3)
'''
a    7000.0
c    4500.0
d    3500.0
'''

# 4. Series 연산 

# 1) 범위 수정 
print(ser)
ser[1:4] = 5.0
print(ser)

# 2) broadcast 연산 
print(ser * 0.5) # 1차원 * 0차원(상수)
'''
lst = [1,2,3,4]
lst * 0.5 # TypeError
'''

# 3) 수학/통계 함수 
dir(ser)
ser.mean() # 평균
ser.sum() # 합계
ser.var() #  분산
ser.std() # 표준편차
ser.max() # 최댓값
ser.min() # 최솟값
ser.mode() # 최빈수 
# 0    5.0

ser.value_counts() # 빈도분석 
'''
5.0     3
4.0     1
10.5    1
'''

ser.unique() # 유일값 
# array([ 4. ,  5. , 10.5])


############################
### 결측치(NaN)
############################
'''
NaN : Not a Number 
- 잘못된 입력으로 인해서 계산 불가 경우 -> NaN 반환 
  ex) 음수에 제곱근(sqrt) 
'''

import numpy as np # 별칭 

test = Series([10, -20])
dir(test)

np.sqrt(test)
'''
0    3.162278  : 정상 입력 
1         NaN  : 비정상 입력 
'''

# 결측치 표현 : np.NaN
score = pd.Series([80, 90, np.NaN, 30])
score
'''
0    80.0
1    90.0
2     NaN
3    30.0
'''
dir(score)

# 결측치 확인 
score.isna() # NaN -> True
score.isnull() # NaN -> True

# isnull 반대 반환 
score.notna() # isna() 반대 
score.notnull() # isnull() 반대 

# 결측치 처리 : 중위수 대체 
new_score = score.fillna(score.median()) # new object 
new_score
'''
0    80.0
1    90.0
2    80.0
3    30.0
'''





















