'''
우편번호 찾기 - 52,144개
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소] 
[135-807]  서울  강남구  개포1동 우성3차아파트  (1∼6동)
[135-807]  서울  강남구  개포1동 우성3차아파트 [세부주소 없음]
'''

# 파일 경로 
path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data'

try :   
    dong = input('찾을 동을 입력하세요 : ') # 개포 
    # 우편번호 파일 읽기 
    file = open(path + '/zipcode.txt', mode = 'r', encoding='utf-8')
    line = file.readline() # 첫줄 읽기  
    
    cnt = 0
    while line : # EoF(False)  
        token = line.split('\t') # tab키 
        
        if token[3].startswith(dong) : # 접두어 비교 
            print('['+token[0]+']', token[1], token[2], token[3], token[4])
            cnt += 1
            
        line = file.readline() # 두번째 줄 ~ end줄
        
    print('검색된 주소 개수 : ', cnt)
     
except Exception as e :
    print('Error 발생 : ', e)    
finally :
    file.close() # 객체 닫기  
    
    
    
    
    
    
    
