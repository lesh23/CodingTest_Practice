# -*- coding: utf-8 -*-
"""
정규 표현식(Regular Expressions)  
 - 특정한 규칙을 가진 메타문자를 이용하여 패턴을 지정한 문자열 표현 
 
[주요 메타문자]
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.) 
x* : x가 0번 이상 반복(없는 경우 포함)
x+ : x가 1회 이상 반복
x? : x가 0 ~ 1회 존재
x{m, n} : x가 m~n 사이 연속 
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
| : or 조건식 
\ : 이스케이프 문자를 일반문자로 인식
\d : 숫자 
\w : 단어 
\s : 공백 
() : 그룹핑, 추출할 패턴 지정  
"""

import re # 모듈(re.py) - 방법1 : re.함수()
#import 모듈명(함수명 or 클래스명) 
dir(re) # 함수명 or 클래스명 확인 

from re import findall, match, sub, search # 방법2 : 함수()
#from 모듈명 import 함수명 or 클래스명 

#from re import * # 방법3

# 1. re.findall('pattern', string) 
# - 문자열에서 패턴과 일치하는 문자열을 list 반환  

st1 = '1234 abc홍길동 ABC_555_6 이사도시' # 실습 텍스트 

# 1) 숫자 찾기 : 메타문자([x], x{n}, |) 이용   
print(re.findall('1234', st1)) # ['1234']
print(re.findall('[0-9]', st1)) # ['1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall('[0-9]{3}', st1)) # ['123', '555']
print(re.findall('[0-9]{3,}', st1)) # ['1234', '555']
print(re.findall('[0-9]{1,3}', st1)) # ['123', '4', '555', '6']
print(re.findall('[0-9]{3,4}', st1)) # ['1234', '555']

# 2) 문자열 찾기 : 메타문자(|) 이용 
print(findall('[가-힣]{3,}', st1)) # ['홍길동', '이사도시']
print(findall('[a-z]{3}', st1)) # ['abc']
print(findall('[a-z|A-Z]{3}', st1)) # ['abc', 'ABC']

    
# 3) 접두어/접미어, 중간 문자열 찾기 : 메타문자(^, $, .)
st2 = 'test1abcABC 123mbc abbc,ac 45text' # 실습 텍스트 

print(findall('^test', st2)) # ['test']
print(findall('^text', st2)) # []
print(findall('text$', st2)) # ['text']

# 문자열 중간에서 문자 찾기 : 메타문자(.) 
findall('.bc', st2) # ['abc', 'mbc', 'bbc']
findall('b.', st2) # ['bc', 'bc', 'bb']

e_mail = ['aaa@naver.com', '12aaa@naver.com', 'bbb@naver.com']

for e in e_mail :
    result = findall('^[a-z|A-Z]', e)
    #print(result)
    if result : # [] : False
        print(e)
        

# [문제] 'http://news'로 시작하는 url 추출하기  
urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']

# list + for : 블럭 표현 
final_urls = [] # 옳바른 url 저장 
for url in urls :
    if findall('^http://news', url) : # [] : False 
        final_urls.append(url)

print(final_urls) # ['http://news.com/test', 'http://news.com/test2']


# list 내포 : 한 줄 표현 
final_urls = [url for url in urls if findall('^http://news', url)] # 형식2)
print(final_urls) # ['http://news.com/test', 'http://news.com/test2']


# 4) 단어(word) : 메타문자(\w) - 단어구성 : 한글,영문,숫자(제외:특수문자,공백)
st3 = 'test^홍길동 abc 대한*민국 123$tbc' # 실습 텍스트 

words = findall('\w{2,}', st3)
print(words) # ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']


# 5) 문자열 제외 : 메타문자([^제외문자]) - 불용어 제거 
print(findall('[^t]+', st3)) # t제외한 나머지 문자 1개 이상(+) 

# 불용어 제거 : 공백(\s), 특수문자(^, *, $)
words2 = findall('[^^*$\s]+', st3)
print(words2) # ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']


# 2. re.match(pattern, string) 
# - 문자열(string)에서 패턴과 일치하는 문자열이 있는지 여부 반환  

jumin = '123456-3234567'
type(jumin) # str

'''
\w : 단어 
\d : 숫자
\s : 공백 
'''

result = match('\d{6}-[1-4]\d{6}', jumin) 
# 패터 일치 여부 반환 : 일치 -> object 반환, 불일치 -> NULL 반환 
print(result) # <re.Match object; span=(0, 14), match='123456-3234567'>
'''
span : 일치된 문자열 범위 
match : 일치된 문자열    
'''

jumin_x = '123456-5234567'
result2 = match('\d{6}-[1-4]\d{6}', jumin_x) 
print(result2) # None

if result2 : # object 반환 : True,  None : False 
    print('주민번호 양식')
else :
    print('잘못된 양식')


jumin_x2 = 'ee123456-3234567'
result3 = match('\d{6}-[1-4]\d{6}', jumin_x2)
print(result3) # None


# 3. re.sub(pattern, rep, string) 
# - 문자열(string)에서 패턴과 일치하는 문자열을 찾아서 다른 문자여로 교체 

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text = sub('[\^\*\$]', '', st3) # 특수문자 제거   
print(text) # test홍길동 abc 대한민국 123tbc


# 4. re.search(pattern, string)
# - 문자열(string)에서 패턴과 일치하는 문자열을 검색  

'''
match : 패턴과 문자열이 완벽한게 일치된 경우 
search : 패턴과 부분 문자열이 일치된 경우   
'''

text = "<span> <head> 안녕하세요. </head> </span>"

head = search("<head>.*</head>", text) 
head # <re.Match object; span=(7, 28), match='<head> 안녕하세요. </head>'>

dir(head)
# 매칭된 문자열과 원문 반환 방법 
head.group() # '<head> 안녕하세요. </head>'
head.string # '<span> <head> 안녕하세요. </head> </span>'

head = search("<head>.+</head>", text)
head.group() # '<head> 안녕하세요. </head>'

text2 = "<span> <head></head> </span>"
head = search("<head>.*</head>", text2)
head.group() # '<head></head>'
head = search("<head>.+</head>", text2)
head.group() # AttributeError: 매칭된 문자열 없음    
head = search("<head>.?</head>", text2)
head.group() # '<head></head>'

'''
. : 임의의 문자 1개 
x* : x가 0번 이상 반복(0번 또는 1회 이상)
x+ : x가 1회 이상 반복(0번 제외)
x? : x가 0 ~ 1회 존재(0번 또는 1회)
'''

# 5. re.compile(pattern) 
# - 패턴을 객체로 생성하여 반복 사용
# - 1개 객체로 다기능 수행(findall, macth, search) 

urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']
print(urls, len(urls)) # 4

# url 패턴 객체 생성 
url_pat = re.compile('^http://news')

dir(url_pat)
'''
findall : 문자열 반환
match : 패턴 일치된 완벽한 문자열 여부 
search : 패턴 일치된 부분 문자열 여부  
split : 패턴을 기준으로 문자열 분리 
sub : 패턴을 다른 문자열 교체  
'''

# 1) findall
url_re = [url for url in urls  if url_pat.findall(url)]    
print(url_re)

# 2) match
url_re = [url for url in urls  if url_pat.match(url)]    
print(url_re)

# 3) search
url_re = [url for url in urls  if url_pat.search(url)]  
print(url_re)

# 4) split
str_list = ['우리나라_and대한_and민국', '대한민국_and나라']

# '구분자'로 패턴 객체 만들기 
pat = re.compile('_and')


# 문장 단위 단어 추출 
words = []

for st in str_list :
    words.append(pat.split(st)) # 문장단위 단어집 : 중첩리스트 
    #words.extend(pat.split(st)) # 단어집 : 단일리스트 
    
print(words) # [['우리나라', '대한', '민국'], ['대한민국', '나라']]


# 각 문장에서 첫번째 단어 추출 
first_words = []

for st in str_list :
    result = pat.split(st) # 패턴으로 문자열 분리 
    first_words.append(result[0]) # 오른쪽 문자열 : result[-1]

print(first_words) # ['우리나라', '대한민국']









