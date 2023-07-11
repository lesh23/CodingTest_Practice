''' 정규식 '''
### exam01
'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

  <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''
import re
from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
names = []

for i in emp :
    names += (findall('[가-힣]{2,}', i))



### exam02
'''
문2) 다음과 같은 여러 줄의 문자열을 대상으로 정규표현식을
       적용하여 email 양식이 올바른 것만 출력되도록 하시오. 
       
  <email 양식 조건> 
        아이디 : 첫자는 영문소문자(^[a-z]), 단어길이 3자 이상(\w{3,})
        호스트이름 : 영문소문자 시작([a-z]), 단어길이 2자 이상(\w{2,})
        최상위 도메인 : 영문소문자 3자리 이하([a-z]{3})
        
  << 출력 결과 >>
  you2@naver.com
  kimjs@gmail.com
'''

from re import match # match 함수 이용 
# 정규표현식 기본 패턴 : '메타문자@메타문자.메타문자'

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

email = email.split('\n')

for e in email :        
    result = match('^[a-z]\w{3,}@[a-z]\w{2,}.[a-z]{,3}', e)
    if result :
        print(e) 



# exam03
'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
     힌트) 정규표현식, replace(old, new)함수 이용 
    
   <출력 예시> 
kim 750905-*******
lee 850905-*******
park 770210-*******  
'''

import re # 정규표현식 패키지 임포트
# re.findall, re.compile, re.match 중 하나 이용 

person = """kim 750905-2049118
lee 850905-1059119
choi 790101-5142142
park 770210-1542001"""


for p in person.split(sep='\n') : # 줄 단위 분리 
    result = match('[a-zA-Z]+\s?\d{6}-[1-4]\d{6}$', p)
    #print(result)
    if result :
        print(re.sub('[1-4]\d{6}$','*******',p))
    

    
# exam04
'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경 

# 2. 숫자 제거 

# 3. 문장부호 제거 

# 4. 영문자 제거 

# 5. 특수문자 제거 

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)




