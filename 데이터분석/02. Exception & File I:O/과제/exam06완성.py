''' 
문6) emp.csv 파일을 읽어와서 다음과 같이 처리하시오.
    조건1> 급여(Pay)가 200 이상인 관측치를 df에 저장 & 출력 
    조건2> df를 대상으로 급여 합계와 평균 출력하기
    조건3> 사번(No)이 홀수인 관측치를 df2에 저장 & 출력
    조건4> 사원명(Name)이 '신'으로 끝나는 관측치를 df3에 저장 & 출력(난이도 : 상)
    
    
 <<조건1 출력 결과>>
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400  

 <<조건2 출력 결과>>
급여 합계 : 1,700   : pay.sum()
급여 평균 : 425.00  : pay.mean()

 <<조건3 출력 결과>>
    No Name  Pay
0  101  홍길동  150
2  103  강감찬  500
4  105  김유신  400

 <<조건4 출력 결과>>
    No Name  Pay
1  102  이순신  450
4  105  김유신  400
'''

import pandas as pd

path = r"C:\ITWILL\2_Python\workspace\chap08_FileIO\data" # file 경로

emp = pd.read_csv(path + '/emp.csv')

print(emp.info()) # 칼럼 정보 
'''
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
'''
print(emp) # 내용 확인 
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

# 조건1> 급여(Pay)가 200 이상인 관측치를 df에 저장 & 출력 
df = emp[emp.Pay >= 200]
print(df)

# 조건2> df를 대상으로 급여 합계와 평균 출력하기
pay = df.Pay # 급여 칼럼 추출 
print('급여 합계 : {0:3,d}'.format(pay.sum()))
print('급여 평균 : {0:5.2f}'.format(pay.mean()))

# [참고] 첫단위 콤마와 소숫점 표기 
a = 12345
b = 12345.12345
print(format(a, ',d')) # 12,345
print(format(b, ',.2f')) # 12,345.12


# 조건3> 사번(No)이 홀수인 사원의 관측치를 df2에 저장 & 출력  
df2 = emp[emp.No % 2 != 0]
print(df2)
'''
    No Name  Pay
0  101  홍길동  150
2  103  강감찬  500
4  105  김유신  400
'''

# 조건4> 사원명(Name)이 '신'으로 끝나는 관측치를 df3에 저장 & 출력(난이도 : 상)   
import re # match() 함수이용 

# [실행문 for 변수 in 반복객체]
df3 = emp[emp.Name==[name if re.match('..신$', name) else 'test'
                     for name in emp.Name ]]
print(df3)
'''
    No Name  Pay
1  102  이순신  450
4  105  김유신  400
'''










