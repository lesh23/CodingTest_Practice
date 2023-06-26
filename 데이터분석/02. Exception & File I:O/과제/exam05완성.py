'''
문제5) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : 힌트) set 자료 이용
  단계3 : 중복되지 않은 서울시 전체 동 list 출력 
  
  <출력 예시>  
중복 포함 전체 동 개수 : 8080
서울시 전체 동 개수 = 797

서울시 전체 동 list 출력   
['화양동', '풍납2동', '공릉동', '서울충정로우체국사서함', '도렴동', '교북동',
 '상봉2동', '홍제동', '염곡동', '체부동', '시흥4동', '홍제1동', '잠실3동', 
 '명일동', '묵정동', '신내동', '신설동', '번2동', '하왕십리동', '난곡동', '상계8동', '용문동', '양재2동', '홍지동', '갈현1동', '천호1동', '양평동', '수유3동', '목동', '돈암1동', '내수동', '목1동', '고척1동', '신영동', '대방동', '수유동'
'''

#import pandas as pd
path = r'C:\ITWILL\2_Python\workspace\chap08_FileIO\data'

file = open(path + "/zipcode.txt", mode='r', encoding='utf-8')
lines = file.readline() # 첫줄 읽기 
dong = [] # 서울시 동 저장 list

while lines :
    token = lines.split('\t') # tab키 토큰 생성 
    
    if token[1] == '서울' : # 두번째 토큰과 비교(서울 지역만 선택) 
        dong_data = token[3].split(' ') # 동 정보를 공백으로 분리 
        dong.append(dong_data[0]) # 첫번째 동이름 추가  
        
    lines = file.readline() # 2번째줄 ~ 마지막줄 읽기 

print('중복 포함 전체 동 개수 :', len(dong))
print('서울시 전체 동 개수 =', len(set(dong))) # list -> set변환 

print('서울시 전체 동 list 출력')  
print(list(set(dong))) # set -> list 변환 
  
file.close() # 객체 닫기 












    