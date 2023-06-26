# -*- coding: utf-8 -*-
"""
문7) json 형식을 갖는 usagov_bitly.txt 파일을 읽어와서 다음과 같이 처리하시오.
    단계1> 전체 3,560개 행을 대상으로 url 자료를 추출하여 list에 저장  : decoding 
           -> 'u'키를 이용하여 url자료 추출, 만약 'u'키가 없으면 예외처리  
    단계2> list에 저장된 url 자료를 텍스트 파일 형식의 urls.txt 파일명으로 저장 : encoding      
"""

import json
path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data'

# json file read
file = open(path + "/usagov_bitly.txt", mode='r', encoding='utf-8')
lines = file.readlines() # 줄단위 전체 읽기
file.close()

print('전체 줄 수 :', len(lines)) # 전체 줄 수 : 3560
print(lines) # ['{row1}', '{row2}', ... '{3560}']


# 단계1> 전체 3,560개 행을 대상으로 url 자료를 추출하여 list에 저장  : decoding 
urls = [] # url 저장 

for row in lines : # 한 줄 받기 
    try :
        pyObj = json.loads(row) # decoding : str -> dict 변환 
        urls.append(pyObj['u']) # url 저장 : 예외발생 
    except :
        print('현재 row에 u 키 없음') # 예외발생 메시지 출력 

print('url 개수 :', len(urls)) # url 개수 : 3440  
#3560 - 3440 # 120행 url 키 없음 
 
# 단계2> list에 저장된 url 자료를 텍스트 파일 형식의 urls.txt 파일명으로 저장 : encoding      
file = open(path + '/urls.txt', mode='w', encoding='utf-8')

for url in urls :
    string = json.dumps(url) # encdong : dict -> str
    file.write(string) # json file save 
    file.write('\n') # 줄바꿈 

file.close() # 객체 닫기 





