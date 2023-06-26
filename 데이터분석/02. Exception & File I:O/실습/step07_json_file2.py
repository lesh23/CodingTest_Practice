'''
json 파일 2가지 형식

 1. 중괄호 형식 : dict 형식 json 문자열
    예) {key : value}, {key : value} -> usagov_bitly.txt
    json.loads(row) : str -> dict 
    
 2. 대괄호 형식 : list 형식 json 문자열
    예) [{key : value}, {key : value}] -> labels.json
    json.load(file) : file -> dict 
'''

import json

path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data'


# 1. 중괄호 형식 : dict 형식 json 문자열
file = open(path + "/usagov_bitly.txt", mode='r', encoding='utf-8')
lines = file.readlines() # list 
len(lines) # 3560

# str -> dict 변환 
rows = [ json.loads(row) for  row in lines ] # loads(str)
print(len(rows)) # 3560
file.close()

type(rows[0]) # dict



# 2. 대괄호 형식 : list 형식 json 문자열
file = open(path + "/labels.json", mode='r', encoding='utf-8')

rows = json.load(file) # load(file) -> object 
file.close()

print(type(rows)) # <class 'list'>
print(rows) 

len(rows) # 30
type(rows[0]) # dict














