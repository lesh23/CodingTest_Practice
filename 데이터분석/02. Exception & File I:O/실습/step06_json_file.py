'''
json 파일
 - 네트워크상에서 표준으로 사용되는 파일
 - 파일 형식 : {key:value, key:value}
 - 활용 예 : 서로 다른 플랫폼(java vs python)에서 파일(data) 공유

- json 모듈 기능 
 1. encoding : json file 저장(Python 객체 -> file 저장)
 2. decoding : json file 읽기(file 읽기 -> Python 객체)
'''

import json

path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data'

##########################
### 1. json encoding
##########################

# 1) python dict
user = { 'id': 1234,  'name': '홍길동', 'job':'관리자'} # dict
type(user) # dict

# 2) json 인코딩 : dict -> string, ensure_ascii=False -> 한글 사용시 
jsonString = json.dumps(user, ensure_ascii=False) # ASCII 인코딩 안함
jsonString # '{"id": 1234, "name": "홍길동", "job": "관리자"}'
type(jsonString) # str

# 3) file save 
file = open(path + "/json_test.txt", mode='w', encoding='utf-8')
file.write(jsonString)
file.close()


##########################
### 2. json decoding 
##########################

# 1) json file 읽기
file = open(path + "/json_test.txt", mode='r', encoding='utf-8')
json_txt = file.readline()
file.close()

type(json_txt) # str
json_txt # '{"id": 1234, "name": "홍길동", "job": "관리자"}'
json_txt['id'] # TypeError

# 2) json 디코딩 : string -> dict 
pyObj = json.loads(json_txt)

# 3) python dict
print(pyObj) # {'id': 1234, 'name': '홍길동', 'job': '관리자'}
type(pyObj) # dict
pyObj['name']


#############################
### 3. json file read/write
#############################

# 1) json file read : json 문자열 -> python 객체
file = open(path + "/usagov_bitly.txt", mode='r', encoding='utf-8')
lines = file.readlines() # 줄단위 전체 읽기 : list 반환 
file.close()
print(lines) # [{row1}, {row2}, ''' {3560}]
len(lines) # 3560
type(lines) # list

type(lines[0]) #  str


# 2) decoding : 줄 단위 텍스트 읽기 -> dict객체  -> list 저장 
pyObj = [] # 디코딩 저장 
for row in lines : 
    pyObj.append(json.loads(row)) # loads(str) -> dict 
    
print(pyObj)
pyObj[0] # {key:value, key:value, ...}
first = pyObj[0] 
type(first) # dict
first['a'] # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11'
first['u'] # 'http://www.ncbi.nlm.nih.gov/pubmed/22415991'


# 3) json file write : encoding -> json file save
file = open(path + "/usagov_json.txt", mode='w', encoding='utf-8')

for row in pyObj : # dict -> string -> file save
    # encoding : dict -> str 
    json_str = json.dumps(row)
    file.write(json_str) # file save 
    file.write('\n') # 줄 바꿈 

file.close() 













