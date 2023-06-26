######################################
### 결측치 처리
######################################

'''
- 숫자형 변환과정에서 결측치 처리 

x변수 : 문자형 -> 숫자형 변환 
x변수 : 결측치 처리 
y변수 레이블 인코딩 
'''

import pandas as pd 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 데이터셋 출처 : https://www.kaggle.com/uciml/breast-cancer-wisconsin-data?select=data.csv
cencer = pd.read_csv(r'C:\ITWILL\5_Python_ML\data\brastCencer.csv')
cencer.info()
'''
RangeIndex: 699 entries, 0 to 698
Data columns (total 11 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id               699 non-null    int64  -> 제거 
 1   clump            699 non-null    int64 
 2   cell_size        699 non-null    int64 
 3   cell_shape       699 non-null    int64 
 4   adhesion         699 non-null    int64 
 5   epithlial        699 non-null    int64 
 6   bare_nuclei      699 non-null    object -> x변수(노출원자핵) : 숫자형 변환
 7   chromatin        699 non-null    int64 
 8   normal_nucleoli  699 non-null    int64 
 9   mitoses          699 non-null    int64 
 10  class            699 non-null    int64 -> y변수 
'''


# 1. 변수 제거 
df = cencer.drop(['id'], axis = 1) # 열축 기준 : id 칼럼 제거  
df.shape # (699, 10)


# 변수 형변환 
'''
DF['칼럼명'].astype('자료형')
자료형 : int32/64, float32/64, object, category
'''

# 2. x변수 숫자형 변환 : object -> int형 변환  
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # error 발생 
# ValueError: invalid literal for int() with base 10: '?'

df['bare_nuclei'].unique()
# ['1', '10', '2', '4', '3', '9', '7', '?', '5', '8', '6']


# 3. 특수문자('?') 결측치 처리 & 자료형 변환 

# 1) 특수문자 결측치 대체   
import numpy as np 
df['bare_nuclei'] = df['bare_nuclei'].replace('?', np.nan) # 결측치로 교체 


# 2) 전체 칼럼 단위 결측치 확인 
df.isnull().any() # 1개 이상 결측치 : bare_nuclei         True
df.isnull().sum() # 16

# 3) 결측치 제거  
new_df = df.dropna(subset=['bare_nuclei']) # bare_nuclei 기준 결측치 제거   
new_df.shape # (683, 10) : 16개 제거 
699 - 683 # 16

new_df.info()
# 5   bare_nuclei      683 non-null    object


# 4) int형 변환 : 문자형(object) -> 정수형  
new_df['bare_nuclei'] = new_df['bare_nuclei'].astype('int64') 
new_df.info()


df['class'].value_counts()
'''
2    458  -> 0
4    241  -> 1
'''

# 4. y변수 레이블 인코딩 : 10진수 변환 
from sklearn.preprocessing import LabelEncoder # class 

# 인코딩 객체 
encoder = LabelEncoder().fit(new_df['class']) # object 

# data변환 
labels = encoder.transform(new_df['class']) # 데이터셋 반영  
labels # 0 or 1
 
# x, y변수 전처리  
new_df['y'] = labels 
new_df.info() 
'''
 9   class            683 non-null    int64
 10  y                683 non-null    int64
''' 

new_df[['class','y']].head(10)

# class 칼럼 제거 
new_df.drop('class', axis = 1, inplace = True) # 현재객체 반영 
new_df.info() 
'''
 0   clump            683 non-null    int64
 1   cell_size        683 non-null    int64
 2   cell_shape       683 non-null    int64
 3   adhesion         683 non-null    int64
 4   epithlial        683 non-null    int64
 5   bare_nuclei      683 non-null    int64
 6   chromatin        683 non-null    int64
 7   normal_nucleoli  683 non-null    int64
 8   mitoses          683 non-null    int64
 9   y                683 non-null    int64
'''
