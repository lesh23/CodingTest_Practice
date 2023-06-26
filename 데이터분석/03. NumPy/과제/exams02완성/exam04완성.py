'''
문4) ~/chapter03_Numpy/data 폴더에 포함된 전체 텍스트 파일(*.txt) 전체를 읽어서 리스트에 저장하시오. 
'''


from glob import glob # 파일 검색 패턴 사용

# text file 경로 
path = r"C:\ITWILL\5_Python_ML\workspace\chapter03_Numpy" # 파일 기본 경로 

full_text = [] # 텍스트 저장 list 

for file in glob(path + '/data/*.txt') :
    #print(file) # 파일 경로 확인 
    file = open(file=file, mode='r', encoding='utf-8') # file 객체 
    text_data = file.read() # 전체 읽기 
    file.close() # 객체 닫기 
    full_text.append(text_data)
    
# 텍스트 확인 
print(full_text)    
len(full_text) # 5   

 
    
    
    