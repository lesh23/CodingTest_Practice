'''
lecture01 > step02 관련문제

문3) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     <단계1> : 파일 가져오기, 정보 확인 
     <단계2> : y변수 : diagnosis 
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd

path = r"c:/ITWILL/5_Python_ML/data" # file 경로 변경 

# <단계1> : 파일 가져오기, 정보 확인 
wdbc = pd.read_csv(path + '/wdbc_data.csv')
wdbc.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568 -> 관측치 
Data columns (total 32 columns):  -> 32개 칼럼 
'''
    
# <단계2> : y변수, x변수 선택
  
# y변수 : diagnosis
y = wdbc['diagnosis'] # 단일칼럼 : 단일list 
# y = wdbc.diagnosis
y.shape # (569,) : 1차원(1개 변수) 

# x변수 : id 칼럼 제외  나머지 30개 칼럼
names = list(wdbc.columns)
names # 3번째 이후 변수 선택 

x = wdbc[names[2:]]
x.shape # (569, 30) : 2차원(30개 변수)
x.head() # radius_mean ~ dimension_worst




  
