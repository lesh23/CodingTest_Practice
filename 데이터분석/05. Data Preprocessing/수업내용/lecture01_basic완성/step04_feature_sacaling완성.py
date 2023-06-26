#########################################
### 4. 피처 스케일링(feature scaling) 
#########################################

"""
피처 스케일링 : 서로 다른 크기(단위)를 갖는 X변수(feature)를 대상으로 일정한 범위로 조정하는 전처리 작업 
 - 방법 : 표준화, 최소-최대 정규화, 로그변환    
 
 1. 표준화 : X변수를 대상으로 정규분포가 될 수 있도록 평균=0, 표준편차=1로 통일 시킴 
   -> 회귀모델, SVM 계열은 X변수가 정규분포라고 가정하에 학습이 진행되므로 표준화를 적용   
 2. 최소-최대 정규화 : 서로 다른 척도(값의 범위)를 갖는 X변수를 대상으로 최솟값=0, 최댓값=1로 통일 시킴 
   -> 트리모델 계열(회귀모델 계열이 아닌 경우)에서 서로 다른 척도를 갖는 경우 적용 
 3. 로그변환 : log()함수 이용하여 로그변환   
   -> 비선형(곡선) -> 선형(직선)으로 변환
   -> 왜곡을 갖는 분포 -> 좌우대칭의 정규분포로 변환   
   -> 회귀모델에서 Y변수 적용(X변수를 표준화 또는 정규화할 경우 Y변수는 로그변환) 
"""

# 1. 함수형 스케일링 도구  
from sklearn.preprocessing import scale # 표준화 
from sklearn.preprocessing import minmax_scale # 정규화
import numpy as np # 로그변환 + 난수
import pandas as pd  # matrix -> DataFrame 


# 실습 data 생성 : 난수 정수 생성  
np.random.seed(12) # 시드값 
X = np.random.randint(-10, 100, (5, 4)) # -10~100
X.shape # (5, 4)

# matrix -> DataFrame
df = pd.DataFrame(X, columns=['x1','x2','x3','x4'])


# 1) 표준화 
X_zscore = pd.DataFrame(scale(df, axis=0),
                        columns=['x1','x2','x3','x4']) # mean=0, st=1
'''
zscore = (X - mu) / sigma 
'''
X_zscore

# 칼럼 단위 통계 
X_zscore.describe() # mean=0, std=1


# 2) 정규화 
X_nor = pd.DataFrame(minmax_scale(df, axis=0),
                     columns=['x1','x2','x3','x4'])# axis=0 : 열단위 정규화  
'''
X - min(X) / max(X) - min(X)
'''

X_nor.describe() # min=0, max=1


# 3) 로그변환 : y변수 대상  
X_log = np.log(X) # 0 or 음수 -> RuntimeWarning 발생
np.log(0) # -inf
np.log(-1) # nan

np.log1p(0) # log(x+1)
np.log1p(abs(-1)) # 0.6931471805599453

X_log = np.log1p(abs(X))
X_log



# 2. 클래스형 스케일링 도구 
from sklearn.preprocessing import StandardScaler, MinMaxScaler # x변수  
from sklearn.preprocessing import LabelEncoder # y변수 인코딩 

import pandas as pd
iris = pd.read_csv(r"C:\ITWILL\5_Python_ML\data\iris.csv")
iris.info()

# object -> 10진 인코딩 
y = LabelEncoder().fit_transform(y=iris['Species'] )


# 1) DataFrame 표준화 : 회귀계열모델(X변수:표준화, y변수:레이블인코딩) 
scaler = StandardScaler()
# DF -> numpy array  
X_scaled = scaler.fit_transform(X=iris.drop('Species', axis=1))# Species 칼럼 제외 
X_scaled.shape # (150, 4)
type(X_scaled) # numpy.ndarray

# new_df = X_scaled + y
new_df = pd.DataFrame(X_scaled, columns=list(iris.columns[:4]))
new_df.info()
new_df['y'] = y

new_df.info()
new_df.describe()


# 2) DataFrame 정규화 : 트리계열모델(X변수:정규화, y변수:레이블인코딩)
scaler2 = MinMaxScaler()

# DF -> numpy array
X_scaled2 = scaler2.fit_transform(X = iris.drop('Species', axis = 1))

# new_df2 = X_scaled + y
new_df2 = pd.DataFrame(X_scaled2, columns=list(iris.columns[:4]))
new_df2.info()
new_df2['y'] = y

new_df2.info()

new_df2.describe()

