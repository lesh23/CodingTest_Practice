'''
예외처리 예 
  - file/DB 입출력 시 문제 발생  
  - 반복 수행 과정에서 계산이 불가능한 자료 포함
  - url을 이용하여 웹문서를 수집할 경우 해당 url이 없는 경우 

예외처리 형식)  
try :
    예외발생 코드 
except 예외처리클래스 as 변수: 
    예외처리 코드 
finally :
    항상 실행 코드

 
'''
# 1. 반복 수행 과정에서 계산이 불가능한 자료 포함

# 예외처리 전 
print('프로그램 시작 !!!')
x = [10, 20, 5, 30, 'num', 7 ]

for i in x :
    print(i)    
    y = i**2  # 예외 발생 type(s) for ** or pow(): 'str' and 'int'
    print('y =', y)

print('프로그램 종료')

# 예외처리 
print('프로그램 시작 !!!')
x = [10, 20, 5, 30, 'num', 7 ]

for i in x :       
    try :
        print(i)
        y = i**2  # 예외 발생 
        print('y =', y)        
    except Exception as e : # e : 예외정보 
        print('~ 예외발생 ~ : ', e)

print('프로그램 종료')



# 2. 문자열 처리과정에서 에러 처리   

import re 
texts = ["<span><h1>제목1</h1></span>", "<h1></h1>", "<p><h2>제목2</h2></p>"]

# 패턴를 찾아서 내용 출력 
print(re.search("<h.>.+</h.>", texts[0]).group()) # <h1>제목1</h1>
print(re.search("<h.>.+</h.>", texts[1]).group()) # AttributeError : 예외발생 
print(re.search("<h.>.+</h.>", texts[2]).group()) # <h2>제목2</h2>

heads = [] 
for st in texts :
    try : 
        result = re.search("<h.>.+</h.>", st)
        heads.append(result.group()) # 문자열 반환
    except Exception as e :
        print('예외발생 : ', e)        

print(heads) # ['<h1>제목1</h1>', '<h2>제목2</h2>']


    
# 3. 유형별 예외처리 
print('\n유형별 예외처리 ')
try :
    div = 1000 / 2.53   
    print('div = %5.2f' %(div))  # 정상   
    #div = 1000 / 0                  # 1차 산술적 예외 
    #f = open('c:/test.txt')          # 2차 파일 열기
    num = int(input('숫자 입력 : '))  # 3차 기타 예외 
    print('num =', num)  
except ZeroDivisionError as e: # 1차 산술적 예외 처리 
    print('오류 정보 :', e) # 오류 정보  : division by zero
except FileNotFoundError as e: # 2차 파일 열기 처리 
    print('오류 정보 : ', e) 
except Exception as e :        # 3차 기타 예외 처리 
    print('기타 오류 정보 : ', e)
finally :
    print('프로그램 종료 : 항상 실행되는 영역') 
    
    
    
    
    
    
    