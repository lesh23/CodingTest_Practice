# -*- coding: utf-8 -*-
"""
step02_DataFrame.py

DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 Table 구조와 동일함)
 - 칼럼 단위 상이한 자료형 
 - Series(1차원) <-> DataFrame(2차원) 
"""

import pandas as pd # 별칭 : pd.DataFrame()
from pandas import DataFrame 


# 1. DataFrame 객체 생성 

# 1) list와 dict 이용 
names = ['hong', 'lee', 'kim', 'park']
ages = [35, 45, 55, 25]
pays = [250, 350, 450, 250]

# key -> 칼럼명, value -> 칼럼값 
frame = pd.DataFrame({'name':names, 'age': ages, 'pay': pays})
frame 
'''
   name  age  pay
0  hong   35  250
1   lee   45  350
2   kim   55  450
3  park   25  250
'''

# Series(1차원) -> DataFrame(2차원)
gender = pd.Series(['M','F','F','M'])

# df에 칼럼 추가 
frame['gender'] = gender
frame
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  350      F
2   kim   55  450      F
3  park   25  250      M
'''

# DataFrame(2차원) -> Series(1차원) 
pays = frame['pay']
type(pays) # pandas.core.series.Series

print('급여평균 = ', pays.mean())
# 급여평균 =  325.0


dir(frame)


# 객체 정보 
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3   -> 관측치 
Data columns (total 3 columns): -> 칼럼(변수)
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object : 문자형 
 1   age     4 non-null      int64  : 정수형 
 2   pay     4 non-null      int64  : 정수형  
'''
frame.shape # 자료모양 : (4, 3) - 2차원(행,열)


# 2) numpy 객체 이용
import numpy as np

# numpy 이용 자료 생성 
data = np.arange(12).reshape(3, 4) # 1d -> 2d
print(data) 

# numpy -> pandas
frame2 = DataFrame(data, columns=['a','b','c','d'])
frame2
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''


# 2. DF 칼럼 참조 
path = r'C:/ITWILL/5_Python_ML/data' # 경로 지정
emp = pd.read_csv(path + "/emp.csv", encoding='utf-8')
type(emp) # pandas.core.frame.DataFrame
print(emp.info())
print(emp) # 전체 내용 

emp.head() # 칼럼명 + 상위관측치 5개 
emp.tail() # 칼럼명 + 하위관측치 5개

# 1) 단일 칼럼 : 단일 list 
no = emp.No # 방법1 : DF.칼럼명 
name = emp['Name'] # 방법2 : DF['칼럼명']
# 방법2 : 칼럼명에 특수문자 or 공백 있는 경우 

print(no)
print(name)

# 2) 복수 칼럼 : 중첩list  
df = emp[['No','Pay']]  
#df = emp[['No':'Pay']]  # Error 발생 

print(df)
type(df) # pandas.core.frame.DataFrame

cols = ['No','Pay']
df = emp[cols]
df


# 3. subset 만들기 : old DF -> new DF

# 1) 특정 칼럼 선택(칼럼수가 작은 경우)
subset1 =  emp[['Name', 'Pay']]
print(subset1)


# 2) 특정 행 제외 
subset2 = emp.drop([1,3], axis=0) # 2,4행 제외 : 현재 객체 변경 없음 
print(subset2)
'''
    No Name  Pay
0  101  홍길동  150
2  103  강감찬  500
4  105  김유신  400
'''

# 3) 조건식으로 행 선택 : 비교연산자, 논리연산자  
subset3 = emp[emp.Pay > 350] # 비교연산자 : 급여 350 이하 제외 
print(subset3)
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
4  105  김유신  400
'''

# 논리연산자 이용 : &(and), |(or), ~(not) 
emp[(emp.Pay >= 300) & (emp.Pay <= 400)] # 급여 300 ~ 400 사이  
'''
    No Name  Pay
3  104  유관순  350
4  105  김유신  400
'''

# 사번 짝수 or 홍길동 선택 
emp[(emp.No % 2 == 0) | (emp.Name == '홍길동')]
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
3  104  유관순  350
'''

# 홍길동 사원의 제외한 나머지 사원 
subset4 = emp[~(emp.Name == '홍길동')]
subset4


# 칼럼값 이용 : 칼럼.isin([목록])
two_name = emp[emp.Name.isin(['홍길동', '유관순'])] # 2명 선택 
two_name
'''
    No Name  Pay
0  101  홍길동  150
3  104  유관순  350
'''

# 4) columns 이용 : 칼럼이 많은 경우 칼럼명 이용  
iris = pd.read_csv(path + '/iris.csv')
iris.index # RangeIndex(start=0, stop=150, step=1)
iris.columns 
# Index(['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species'],

# 방법1 : Error 발생 
#iris.Sepal.Length  # AttributeError
# 첫번째 칼럼 : 방법2
iris['Sepal.Length']


names = list(iris.columns) # 전체 칼럼명 list 반환 
names # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

# 변수 선택 
names[:4] # 앞부분 4개 선택 : x
names[-1] # 끝부분 1개 선택 : y
names[1:-1] # 중간 3개 선택 
#names[[0,2,3]] # Error 

# 변수 제외 
names.remove('Petal.Length') # (value) : 반환값 없음 
names # ['Sepal.Length', 'Sepal.Width', 'Petal.Width', 'Species']

# x변수 : 1~4칼럼
iris_x = iris[names[:4]] # iris[['칼럼1', '칼럼2',...]]
iris_x.shape # (150, 4) : 2차원 

# y변수 : 5칼럼 
iris_y = iris[names[-1]] # iris['Species']
iris_y.shape # (150,) : 1차원

# 3번 칼럼 제외 
names # 5개 칼럼 
names.remove('Petal.Length') 
names # ['Sepal.Length', 'Sepal.Width', 'Petal.Width', 'Species']
# x변수 : 1,2,4칼럼 
iris_x = iris[names[:3]]
iris_x.head()

# y변수 : 5칼럼
iris_y = iris[names[-1]] 
iris_y.head()

iris_x.shape # (150, 3)

# 열단위 평균 통계 
iris_x.mean(axis = 0) # 행축 : 열 단위 평균 
'''
Sepal.Length    5.843333
Sepal.Width     3.057333
Petal.Width     1.199333
'''

# 빈도분석 
iris_y.value_counts()
'''
setosa        50
versicolor    50
virginica     50
'''


# 4. DataFrame 행열 참조 
'''
DF.loc[행label, 열label]
DF.iloc[행integer, 열integer]
연속 : 콜론(:)
'''
print(emp)
'''
칼럼 : 명칭(label)
행 : 숫자(integer)
'''
# 1) loc 속성 : 명칭 기반 
emp.loc[0, :] # 1행 전체 
emp.loc[0] # 열 생략 가능 
emp.loc[0:2] # 1~3행 전체 
emp.loc[0:2, ('No','Pay')] # 비연속 명칭기반 행렬 참조
emp.loc[0:2, ['No','Pay']] # 비연속 명칭기반 행렬 참조 
emp.loc[0:2, 'No':'Pay'] # 연속된 명칭 선택 
#emp.loc[0:2, [0,2]] # KeyError

# 2) iloc 속성 : 숫자 위치 기반 
emp.iloc[0] # 1행 전체 
emp.iloc[0:2] # 1~2행 전체 
emp.iloc[0:2, [0,2]] # 숫자기반 행렬참고 
#emp.iloc[0:2, ['No','Pay']] # IndexError

emp.iloc[:,1:] # 2번째 칼럼 이후 연속 칼럼 선택


# exam02 ~ exam04 














