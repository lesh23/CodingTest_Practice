'''  
lecture01 > step02 관련문제

문4) 다음 df를 대상으로 iloc 속성을 이용하여 단계별로 행과 열을 선택하시오.
   <단계1> : 1,3행 전체 선택    
   <단계2> : 1~4열 전체 선택 
   <단계3> : 1,3행 1,3,5열 선택
'''

import pandas as pd # DataFrame 
import numpy as np # dataset 

data = np.arange(1, 16).reshape(3,5) # 3x5
data.shape #  (3, 5)

df = pd.DataFrame(data, index = ['one', 'two', 'three'],
                  columns = [1,2,3,4,5])
'''
index : 행 이름 지정 속성 
columns : 열 이름 지정 속성 
'''

print(df)
'''
        1   2   3   4   5
one     1   2   3   4   5
two     6   7   8   9  10
three  11  12  13  14  15

열(칼럼) : 숫자 색인 
행 : 명칭 색인 
'''

### iloc 속성 : 숫자 색인 ###
# 단계1 : 1,3행 전체 선택
df.iloc[[0,2]] # df.iloc[[0,2],:]
'''
        1   2   3   4   5
one     1   2   3   4   5
three  11  12  13  14  15
'''

# 단계2 : 1~4열 전체 선택 
df.iloc[:, :4]
'''
        1   2   3   4
one     1   2   3   4
two     6   7   8   9
three  11  12  13  14
'''

# 단계3 : 1,3행 1,3,5열 선택
df.iloc[[0,2], [0,2,4]]
'''
        1   3   5
one     1   3   5
three  11  13  15
'''


### loc 속성 : 명칭 색인 ###
print(df)

# 단계1 : 1,3행 전체 선택
df.loc[['one','three']]

# 단계2 : 1~4열 전체 선택
df.loc[:, :4] # 숫자를 명칭으로 해석 

# 단계3 : 1,3행 1,3,5열 선택
df.loc[['one','three'], [1,3,5]] # 숫자를 명칭으로 해석 













