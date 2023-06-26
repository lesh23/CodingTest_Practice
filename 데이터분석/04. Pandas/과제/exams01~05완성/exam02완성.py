''' 
lecture01 > step02 관련문제

문2) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd

path = r"c:/ITWILL/5_Python_ML/data" # file 경로 변경 

score = pd.read_csv(path + '/score.csv')
print(score.info())
#print(score)


# 조건1> tv 칼럼이 0인 관측치 2개 삭제
new_df = score[score.tv > 0] # 방법1) 조건 색인 
new_df = score[~(score.tv == 0)] # 방법2) ~(부정) 이용 
new_df.shape # (8, 6) : 2개 행 제거 


# 조건2> score, academy 칼럼만 추출하여 DataFrame 

# 방법1) 복수칼럼(중첩list)
new_df2 = new_df[['score', 'academy']]  
new_df2.shape # (8, 2) : 4개 열 제거 

# 방법2) columns 속성 이용 
names = list(score.columns)
names # ['name', 'score', 'iq', 'academy', 'game', 'tv']
names.remove('iq') # iq칼럼 제거 
names # ['name', 'score', 'academy', 'game', 'tv']

new_df2 = new_df[names[1:3]] #  'score', 'academy' 선택  
new_df2.shape # (8, 2)

# 조건3> score, academy 칼럼의 평균 계산
print(new_df2)
print(new_df2.mean(axis=0)) # 행축(default) : 열단위 평균
'''
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625
'''










