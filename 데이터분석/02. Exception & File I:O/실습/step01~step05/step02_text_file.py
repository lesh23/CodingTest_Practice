'''
텍스트 파일 입출력(file input/output)
 - 데이터 입출력 시(file, db) 예외 처리한다.
 형식) open('파일경로/파일명', mode='r'/'w'/'a')
        mode = 'r' : 파일 읽기
        mode = 'w' : 파일 쓰기
        mode = 'a' : 파일 쓰기 + 추가
        
open() : 텍스트 파일, html파일, json 파일         
'''

import os # 경로 확인, 이동, 생성 

try :
    # 파일 경로 확인 
    print('\n현재 경로 :', os.getcwd())  
    
    # 파일 경로 이동 
    os.chdir(r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data') 
    
    # 1. 파일 읽기 
    file = open("ftest.txt", mode = 'r') # 1. 생성 
    dir(file)
    print(file.read()) # 2. 사용 : 파일 전체 읽기
    file.close() # 3. 객체 닫기
    
    # 2. 파일 쓰기(자동 생성) 
    ftest2 = open('ftest2.txt', mode = 'w') # 1. 생성 
    ftest2.write('my first text~~~') # 2. 사용 : 파일 쓰기 
    ftest2.close() # 3. 객체 닫기 
    
    
    # 3. 파일 쓰기(내용 추가)
    ftest3 = open('ftest2.txt', mode='a') # 1. 생성
    ftest3.write('\nmy second text~~~') # 2. 사용 
    ftest3.close() # 3. 객체 닫기
    
    # 4. 파일 읽기 유형 
    '''
    read() : 모든 줄을 문자열로 읽음 : string 반환 
    readline() : 한 줄 읽기 : string 반환 
    readlines() : 전체 줄을 줄단위 읽기 : list 반환 
    '''
    file = open("ftest.txt", mode = 'r') # 1. 생성
    '''
    text_str = file.read() 
    print(text_str)
    print(type(text_str)) # <class 'str'>
    '''
    '''
    print('='*30)
    while True :        
        line = file.readline()
        if line != '' : # EoF 판단 
            print(line.strip()) # programming is fun
            #print(type(line)) # <class 'str'>
        else :
            print('EoF')
            break # loof 탈출(exit)      
    '''
    lines = file.readlines()
    print(lines) # [문장1, 문장2,...]
    print(type(lines)) # <class 'list'>
    
    for row in lines :
        print(row.strip()) # 문장끝 불용어 제거(\n)
        
    print('문장 길이 : ', len(lines)) # 문장 길이 :  6
    
          
except Exception as e:
    print('Error 발생 : ', e)












