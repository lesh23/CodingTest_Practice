'''
문2) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

 
import os

# 파일 읽기 
os.chdir(r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data')
file = open("ftest.txt", mode = 'r')

stens = [] # 문장 
words = [] # 단어 

# 1. read 이용 
texts = file.read() # 문자열(string) 반환 
print(texts)

for sten in texts.split('\n') : # 줄바꿈 기준 
    stens.append(sten)
    for word in sten.split(' ') : # 공백 기준  
        words.append(word)

print('문단 내용')
print(stens)
print('문단 길이 :', len(stens))
print('단어 내용')
print(words)
print('단어 길이 :', len(words))
file.close()

# 2. readlines 이용 
file2 = open("ftest.txt", mode = 'r')
lines = file2.readlines() # list 반환 
print(lines)

stens = [] # 문장 
words = [] # 단어 

for sten in lines :
    stens.append(sten.strip()) # 불용어 제거(\n)
    for word in sten.split() : # sten.strip().split(' ') :
        words.append(word)

print('문단 내용')
print(stens)
print('문단 길이 :', len(stens))
print('단어 내용')
print(words)
print('단어 길이 :', len(words))
file.close()













