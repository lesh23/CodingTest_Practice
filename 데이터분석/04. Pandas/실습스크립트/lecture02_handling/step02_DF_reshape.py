# -*- coding: utf-8 -*-
"""
step02_DF_reshape.py

- DataFrame 모양 변경 
"""

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

buy = pd.read_csv(path + '/buy_data.csv')

print(buy.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
'''


# 1. 2차원 -> 1차원 구조 변경
buy_long = buy.stack() 

# 2. 1차원 -> 2차원 구조 변경 
buy_wide = buy_long.unstack()

# 3. 전치행렬 
buy_tran = buy.T

# 4. 중복 행 제거 
buy2 = buy.drop_duplicates() # 중복 행 제거
buy2.shape # (20, 3)

# 5. 특정 칼럼을 index 지정 
new_buy = buy.set_index('Date')
