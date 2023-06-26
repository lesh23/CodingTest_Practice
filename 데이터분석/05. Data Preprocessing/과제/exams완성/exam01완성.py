# 문1) dataset 자료를 이용하여 다음과 같은 단계로 결측치를 처리하시오.

import pandas as pd 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 데이터셋 로드 
dataset = pd.read_csv('C:/itwill/5_Python_ML/data/dataset.csv')
dataset.info()
dataset

# 단계1 : 전체 칼럼 중에서 가장 많은 결측치를 갖는 칼럼 찾기 
dataset.isnull().sum() # job


# 단계2. position 칼럼 기준으로 결측치 제거하여 new_dataset 만들기
help(dataset.dropna)
new_dataset = dataset.dropna(subset='position', axis=0)
new_dataset.shape # (208, 7) 


# 단계3. 전체 칼럼을 대상으로 결측치를 제거하여 new_dataset2 만들기
new_dataset2 = dataset.dropna()
new_dataset2.shape # (198, 7)


# 단계4. dataset의 job 칼럼의 결측치를 0으로 대체하여 현재 객체 반영하기
dataset.job.fillna(0, inplace = True)
#dataset['job'].fillna(0, inplace = True)

# 0으로 채워진 관측치 확인 
dataset[dataset.job == 0].shape # (12, 7)
dataset[dataset.job == 0]

# 0으로 채워진 색인 
dataset[dataset.job == 0].index
# [2, 7, 16, 52, 73, 113, 133, 158, 176, 181, 199, 202]



