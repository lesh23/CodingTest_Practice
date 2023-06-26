# -*- coding: utf-8 -*-
"""
텍스트 전처리 : 특수문자, 불용어 처리 
"""

import re # re 모듈 가져오기 

# 전처리 텍스트  
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']
print(texts)

# list + for 
texts_re = []

for st in texts :
    texts_re.append(st.lower())

texts_re    
    
# 단계1 : 소문자 변경 

# list 내포 : 변수 = [실행문 for]
texts_re = [ st.lower() for st in texts] # 형식1) 
print(texts_re)


# 단계2 : 숫자 제거 : sub('pattern', rep, string)
texts_re2 = [re.sub('[0-9]', '', st) for st in texts_re] # 형식1)
print(texts_re2)

# 단계3 : 문장부호 제거 
punc_str = '[,.?!:;]'
texts_re3 = [re.sub(punc_str, '', st) for st in texts_re2] # 형식1)
print(texts_re3)

# 단계4 : 특수문자 제거 
spec_str = '[@#$%^&*()]'
texts_re4 = [re.sub(spec_str, '', st) for st in texts_re3] # 형식1)
print(texts_re4)
# ['afabasabag', 'abtta a', 'uysfsfa  a']


# 단계5 : white space 제거 : 2개 이상 공백 -> 1개 공백 
texts_re5 = [re.sub('\s+', ' ', st) for st in texts_re4] # 형식1)
print(texts_re5)
# ['afabasabag', 'abtta a', 'uysfsfa a']














