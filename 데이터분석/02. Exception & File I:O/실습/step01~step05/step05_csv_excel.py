'''
csv, excel file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기
'''

import pandas as pd # 별칭 

dir(pd)

##########################
### 1. csv file 
##########################

# 1) file 읽기 및 내용 보기  
path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data' 
bmi = pd.read_csv(path + '/bmi.csv', encoding='utf-8')
 
dir(bmi) # 메서드 확인 

# 칼럼명 & 관측치 정보 
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 : 정수형 
 1   weight  20000 non-null  int64 : 정수형 
 2   label   20000 non-null  object : 문자열(범주형) 
'''

# 자료 확인  
print(bmi.head())
print(bmi.tail())
    
# 2) 칼럼 단위 추출 
height = bmi.height # 객체.칼럼명
weight = bmi['weight'] # 객체['칼럼명']
label = bmi.label


# 3) 칼럼 단위 연산 
print('height mean : ', sum(height) / len(height))
print('weight mean : ', sum(weight) / len(weight))    

print('max height:', max(height)) # max height: 190
print('max weight:', max(weight)) # max weight: 85

dir(height)
print('height mean : ', height.mean())
print('weight mean : ', weight.mean())


# label 빈도수 
dir(label)
label_count = label.value_counts()
print(label_count)
'''
normal    7677
fat       7425
thin      4898
'''


# 4) 행열 참조 : 객체.loc[row, col] or 객체.iloc[row, col]
print(bmi.head())

# [1] loc 속성 : 명칭(label) 기반 
bmi.loc[0, :] # 1행 전체(생략 : 열 전체) 
bmi.loc[0] # 1행 전체(생략 : 열 전체) 
bmi.loc[:4] # 5행 전체([:4])

bmi.loc[:,'height':'label'] # 연속 칼럼 
bmi.loc[:,['height','label']] # 비연속 칼럼 
#bmi.loc[:,[0,2]]

# [2] iloc 속성 : 위치(integer) 기반
bmi.iloc[0]
bmi.iloc[:4] # 4행 

bmi.iloc[:, 0:3] # 연속 칼럼 
bmi.iloc[:, [0, 2]] # 비연속 칼럼 
#bmi.iloc[:, ['height', 'label']]


# 5) 조건 검색 : 산술, 비교, 논리연산자 사용 
print(bmi)
df = bmi[(bmi.height >= 180)] # 비교연산자 
print(df)
df = bmi[(bmi.weight >= 60)] # 비교연산자
print(df)
bmi[(bmi.weight >= 50) & (bmi.weight <= 70)] # 논리연산자 and 
bmi[(bmi.label=='thin') | (bmi.label=='fat')] # 논리연산 or
bmi[~(bmi.label=='normal')] # 논리연산 not


##########################
### 2. excel file 
##########################

# 1) file 읽기 및 내용보기 
ex = pd.ExcelFile(path + '/sam_kospi.xlsx')
kospi = ex.parse('sam_kospi') # ('시트명')
print(kospi)

# 칼럼 정보 
print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
'''
    
# 2) 컬럼 추출 
high = kospi.High # 객체.칼럼명 
low = kospi.Low

# 3) 칼럼 단위 통계  
print('High mean :', high.mean())
print('Low mean :', low.mean())

print(kospi.head())

# 칼럼 추가 
kospi['diff'] = kospi.High - kospi.Low

kospi.info()

# 4) csv file save
kospi.to_csv(path + '/kospi.csv', index=None, 
             encoding='utf-8')









