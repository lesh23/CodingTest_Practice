# -*- coding: utf-8 -*-
"""
문4) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.
  
  <출력 예시>  
전체 단어수 = 4,907개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 205
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""


# 텍스트 전처리 함수
def clean_text(texts) :
    from re import sub
    
    # 1. 소문자 변경     
    texts_re = texts.lower()  # string.lower()
    
    # 2. 숫자 제거 : list 내포
    texts_re2 = sub('[0-9]', '', texts_re) 
    
    # 3. 문장부호 제거 : sub('p', 'r', string)
    punc_str = '[,.?!:;]'    
    texts_re3 = sub(punc_str, '', texts_re2) 
    
    # 4. 특수문자 제거 : sub('p', 'r', string)
    spec_str = '[!@#$%^&*()]'    
    texts_re4 = sub(spec_str, '', texts_re3) 
        
    # 5. 공백(white space) 제거 
    texts_re5 = ' '.join(texts_re4.split()) 
    
    return texts_re5


import os 

try :
    # 1.파일 읽기 : obama.txt
    os.chdir('C:/ITWILL/2_Python/workspace/chap08_FileIO/data')
    rfile = open('obama.txt', mode = 'r') 
    
    # 2. 줄단위 전체 읽기 
    texts = rfile.readlines()    
    
    # 3.줄 단위 텍스트 전처리 : 한 문장씩 함수에 넘김     
    texts_re = [clean_text(sten) for sten in texts]    
    
    # 4. 단어 카운트 : 전체 단어수 & 최고 단어 
    words = [] # 단어 
    for st in texts_re :
        for word in st.split() :
            words.append(word)
    print('\n전체 단어수 = {0:3,d}개'.format(len(words)))
          
    wc = {} # 단어 빈도수 
    for word in words :
        wc[word] = wc.get(word, 0) + 1
    
    # 5. Top10 단어 & 단어 빈도수
    wc_sorted = sorted(wc, key=wc.get, reverse=True) # 빈도수 정렬 
    Top10 = wc_sorted[:10] # Top10 단어 선정   
    
    print('최고 출현 단어 :', max(wc, key=wc.get)) # Top10[0] 
    print('top10 word =', Top10)
    print('\n단어 빈도수')
    for word in Top10 :
        print(word, ':' , wc[word])
    
except Exception as e:
    print('Error 발생 : ', e)
finally:
    rfile.close()
    
    
    
    
    
    
    
    
    
    
    
    
    