# 문2) mtcars 자료를 이용하여 다음과 같은 단계로 이상치를 처리하시오.

import pandas as pd 
import seaborn as sn # 데이터셋 로드 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정
import matplotlib.pyplot as plt # boxplot 시각화 

# 데이터셋 로드 
data = sn.load_dataset('mpg')
data.info()
print(data)

# 단계1. boxplot으로 'acceleration' 칼럼의 이상치 탐색 
plt.boxplot(data['acceleration']) # 상한값 이상치 
plt.show()


# 단계2. IQR 방식으로 이상치 탐색
# 1) IQR 수식 작성 
des = data.describe()
Q3 = des.loc['75%', 'acceleration'] #51.0
Q1 = des.loc['25%', 'acceleration'] #27.0
IQR = Q3 - Q1
IQR # 3.3499999999999996

outlier_step = 1.5 * IQR # 5.0249999999999995

minval = Q1 - outlier_step
maxval = Q3 + outlier_step
print(f'minval : {minval}, maxval : {maxval}')
# minval : 8.8, maxval : 22.2

# 2) 이상치 확인 
data[(data['acceleration'] < minval) | (data['acceleration'] > maxval) ]
'''
      mpg  cylinders  displacement  horsepower  weight  acceleration  \
7    14.0          8         440.0       215.0    4312           8.5   
9    15.0          8         390.0       190.0    3850           8.5   
11   14.0          8         340.0       160.0    3609           8.0   
59   23.0          4          97.0        54.0    2254          23.5   
299  27.2          4         141.0        71.0    3190          24.8   
326  43.4          4          90.0        48.0    2335          23.7   
394  44.0          4          97.0        52.0    2130          24.6 
'''


# 단계3. 이상치 대체 : 정상범주의 하한값과 상한값 대체 
low_idx = data[data['acceleration'] < minval].index  # 색인 추출 : Int64Index([12, 114, 180])
data.loc[low_idx, 'acceleration'] = minval # 상한값 대체  
print(data.loc[low_idx]) # 3개 관측치 : 대체 결과 확인 


high_idx = data[data['acceleration'] > maxval].index  # 색인 추출 : Int64Index([12, 114, 180])
data.loc[high_idx, 'acceleration'] = maxval # 상한값 대체  
print(data.loc[high_idx]) # 4개 관측치 : 대체 결과 확인


# 단계4. boxplot으로 'acceleration' 칼럼 이상치 처리결과 확인  
plt.boxplot(data['acceleration']) # 상한값 이상치 
plt.show()



