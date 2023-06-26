
######################################
### 2. 이상치 처리 
######################################
"""
 이상치(outlier) 처리 : 정상범주에서 벗어난 값(극단적으로 크거나 작은 값) 처리  
  - 이상치 제거 & 상수 대체
  - IQR(Inter Quentile Range) 방식으로 탐색과 대체  
"""

import pandas as pd 

data = pd.read_csv(r"C:\ITWILL\5_Python_ML\data\insurance.csv")
data.info()
'''
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64
'''
 
# 1. 범주형 이상치 탐색  
data.sex.unique() # array(['female', 'male']
data.smoker.unique() #  array(['yes', 'no']
data.region.unique() # array(['southwest', 'southeast', 'northwest', 'northeast']


# 2. 숫자형 변수 이상치 탐색  
des = data.describe()
print(des)
'''
               age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.730194    30.524488     1.094918  13270.422265
std      20.224425     6.759717     1.205493  12110.011237
min      18.000000   -37.620000     0.000000   1121.873900
25%      27.000000    26.220000     0.000000   4740.287150
50%      39.000000    30.332500     1.000000   9382.033000
75%      51.000000    34.656250     2.000000  16639.912515
max     552.000000    53.130000     5.000000  63770.428010

age : 최댓값 이상치 
bmi : 최솟값 이상치 
'''

# 3. boxplot 이상치 탐색 
import matplotlib.pyplot as plt

plt.boxplot(data['age']) # 나이 변수 상한값 이상치  
plt.show()

plt.boxplot(data['bmi']) # bmi 변수 하한값/상한값 이상치  
plt.show()

plt.boxplot(data['charges']) # charges 변수 상한값 이상치  
plt.show()


# 4. 이상치 제거 : 관측치가 적고, 해당 변수의 의미를 알고있는 경우 
new_data = data[data['bmi'] > 0] # bmi 변수 음수값 제거 
new_data.info() # Int64Index: 1335 entries, 0 to 1337 : 3행 제거됨 
new_data.shape # (1335, 7) : 3개 row 제거(1338 - 1335)

# 5. 이상치 대체 : 해당 변수의 의미를 알고있는 경우
new_data2 = data.copy() 

data[data['age'] > 100] # 100세 이상 확인 
idx = data[data['age'] > 100].index 
idx # [12, 114, 180]

# 100세 이상 -> 100세 교체 
new_data2.loc[idx, 'age'] = 100
new_data2.shape # (1338, 7) 


# 6. IQR방식 이상치 발견 및 대체 : 해당 변수의 의미를 모르는 경우 

'''
 IQR = Q3 - Q1 : 제3사분위수 - 제1사분위수
 outlier_step = 1.5 * IQR
 정상범위 : Q1 - outlier_step ~ Q3 + outlier_step
'''

# age 칼럼 기준 
print(des)

Q1 = des.loc['25%','age']
Q3 = des.loc['75%','age']

IQR = Q3 - Q1
outlier_step = 1.5 * IQR
outlier_step # 36.0

minval = Q1 - outlier_step
minval # -9.0 -> 0

minval = 0 # 비율척도(절대0점을 갖는 변수)
maxval = Q3 + outlier_step

maxval # 87.0
# 정상범주 : 0 ~ 87

new_data3 = data[(data.age >= minval) & (data.age <= maxval)]
new_data3.shape  # (1335, 7)

plt.boxplot(new_data3['age']) # 나이 변수 이상치 확인  
plt.show()

'''
문) data의 charges 칼럼을 대상으로 이상치를 탐색하여 이상치를 제거하시오.
'''

Q1 = des.loc['25%','charges']
Q3 = des.loc['75%','charges']

IQR = Q3 - Q1
outlier_step = 1.5 * IQR
outlier_step # 17849.4380475

minval = 0 # 비율척도(절대0점을 갖는 변수)
maxval = Q3 + outlier_step

new_data4 = data[(data['charges'] >= minval) & (data['charges'] <= maxval)] 
new_data4.shape # (1199, 7)

1338 - 1199 # 139행 제거 

plt.boxplot(new_data4['charges']) # charges 변수 이상치 확인  
plt.show()





 
