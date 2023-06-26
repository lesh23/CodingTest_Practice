# -*- coding: utf-8 -*-
"""
step03_word_count.py

단어 카운트 작업절차 
 1. 텍스트 파일 읽기
 2. 텍스트 전처리
 3. 단어 카운트
 4. TopN 단어 선정
"""


# 텍스트 전처리 함수 : chap06 > step03 참고 
def clean_text(texts) :     
    from re import sub # re 모듈 가져오기
    
    # [추가] 불용어 제거    
    texts_re = [ st.strip() for st in texts] # '\n' 제거 

    # 단계1 : 소문자 변경   
    texts_re = [ st.lower() for st in texts_re]
        
    # 단계2 : 숫자 제거 
    texts_re2 = [sub('[0-9]', '', st) for st in texts_re]
    
    
    # 단계3 : 문장부호 제거 
    punc_str = '[,.?!:;]'
    texts_re3 = [sub(punc_str, '', st) for st in texts_re2]
    
    
    # 단계4 : 특수문자 제거 
    spec_str = '[@#$%^&*()]'
    texts_re4 = [sub(spec_str, '', st) for st in texts_re3]
    
    
    # 단계5 : 2칸 이상 공백(white space) 제거 -> 1칸 공백 
    texts_re5 = [' '.join(st.split()) for st in texts_re4 ]
    
    return texts_re5


import os # 파일 경로 설정 모듈 

# 1. 텍스트 파일 읽기 
os.chdir('C:/ITWILL/2_Python/workspace/chap08_FileIO/data/')
file = open('texts.txt', mode = 'r', encoding='utf-8') 

texts = file.readlines() # list 반환 
file.close()

print(texts)
# ['우리나라    대한민국, 우리나라%$ 만세\n', '비아그&라 500GRAM 정력 최고!\n', '나는 대한민국 사람\n', '보험료 15000원에 평생 보장 마감 임박\n', '나는 홍길동']


# 2. 텍스트 전처리 
new_texts = clean_text(texts)    
print('전처리 후 : ', new_texts)

# 3 단어 카운트(출현빈도)

# 1) 단어 생성 
words = [] 
for st in new_texts : # 문장 추출 
    for word in st.split(): # 문장 -> 단어 추출 
        words.append(word)
print(words, len(words)) # 19        

# 2) 단어 카운트 
word_count = {} # 기본 셋 
for word in words :
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'우리나라': 2, '대한민국': 2, '만세': 1, '비아그라': 1, 'gram': 1, '정력': 1, '최고': 1, '나는': 2, '사람': 1, '보험료': 1, '원에': 1, '평생': 1, '보장': 1, '마감': 1, '임박': 1, '홍길동': 1}

# 4. TopN 단어 출력 : dict 자료, value 기준, 내림차순  
wc_sorted = sorted(word_count, key=word_count.get, reverse=True) # 내림차순    
print(wc_sorted)
# ['우리나라', '대한민국', '나는', '만세', '비아그라', 'gram', '정력', '최고', '사람', '보험료', '원에', '평생', '보장', '마감', '임박', '홍길동']

TopN = 5
Top5 = wc_sorted[:TopN]
print(Top5) # ['우리나라', '대한민국', '나는', '만세', '비아그라']

'''
단어 -> 출현빈도 
'''
for word in Top5 :
    print(word, '->', word_count[word])
'''
우리나라 -> 2
대한민국 -> 2
나는 -> 2
만세 -> 1
비아그라 -> 1
'''
  