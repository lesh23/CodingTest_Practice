'''   
lecture02 > step01 관련문제

문6) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

path = r'C:\ITWILL\5_Python_ML\data' # file 경로 변경 

iris = pd.read_csv(path + '/iris.csv')
print(iris.info())

# <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']

# <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기
col1.sum() # 합계
col1.mean() # 평균 
col1.std() # 표준편차 

col4.sum() # 합계
col4.mean() # 평균 
col4.std() # 표준편차 

# <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.DataFrame({'col1':col1, 'col2':col2})
df2 = pd.DataFrame({'col3':col3, 'col4':col4})

# <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성
iris_df = pd.concat(objs=[df1, df2], axis=1)
iris_df.shape # (150, 4)

iris_df.head()
iris_df.tail()






