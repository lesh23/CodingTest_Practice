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
    print(p)
    