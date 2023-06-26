# -*- coding: utf-8 -*-
"""
step03_csvFileIO.py

1. csv file read
2. data 처리 : 파생변수 추가 
3. csv file write
"""

import pandas as pd 
import os # 경로 변경 

path = r'C:\ITWILL\5_Python_ML\data'
os.chdir(path)


# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv('student.csv', header=None)
st # 0     1    2   3 -> 기본 칼럼명 

# 칼럼명 수정 
col_names = ['sno','name','height','weight'] # list 
st.columns = col_names # 칼럼 수정 
print(st)


# 2) 칼럼명 특수문자(.) or 공백 
iris = pd.read_csv('iris.csv')
print(iris.info())

#iris.Sepal.Length # AttributeError

# 점(.) -> 언더바(_) 교체 
iris.columns = iris.columns.str.replace('.','_') # ('old','new')
iris.info() # Sepal_Length
iris.Sepal_Length


# 3) 특수구분자(tab키), 천단위 콤마 
# pd.read_csv('file', delimiter='\t', thousands=',')


# 2. data 처리 : 파생변수 추가 
'''
비만도 지수(bmi) = 몸무게/(키**2)
'''
st.info()
bmi = st.weight / (st.height*0.01)**2
bmi
    
# 파생변수 추가 
st['bmi'] = bmi
st.info()

'''
label : normal, fat, thin 
normal : bmi : 18 ~ 23
fat : 23 초과
thin : 18 미만  
'''

st
'''
   sno  name  height  weight        bmi   label 
0  101  hong     175      65  21.224490   normal
1  201   lee     185      85  24.835646    fat
2  301   kim     173      60  20.047446   normal
3  401  park     180      70  21.604938   normal
'''

label = [] 
bmi = st.bmi

for b in bmi :
    if b >= 18 and b <= 23 : # 정상 
        label.append('normal')
    elif b > 23 :  # 비만
        label.append('fat')
    else :
        label.append('thin')
    
st['label'] = label        
st 
'''
   sno  name  height  weight        bmi   label
0  101  hong     175      65  21.224490  normal
1  201   lee     185      85  24.835646     fat
2  301   kim     173      60  20.047446  normal
3  401  park     180      70  21.604938  normal
'''


# 3. csv file 저장 
st.to_csv('st_info.csv', index = None, encoding='utf-8')










