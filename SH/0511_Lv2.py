# 최댓값과 최솟값
def solution(s):
    l = list(map(int, s.split(' ')))
    answer = str(min(l)) + str(' ') +str(max(l))
    return answer

# JadenCase 문자열 만들기
def solution(s):
    # 전부 다 소문자로 만들고
    l=s.lower().split(' ')

    for i in range(len(l)):
        # 맨 앞글자 대문자로 만들고 그 뒤에 나머지꺼 합체
        if len(l[i]) >= 2:
            l[i] = l[i][0].upper() + l[i][1:] 

         # 연속된 공백이라는 문제 조건 고려 & 한글자짜리 고려
        else :
            l[i] = l[i].upper()

    # 공백으로 join        
    return ' '.join(l)

    # 파이썬 내장 함수 이용
    def solution(s):
        return s.title()

# 최솟값 만들기
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]    
    return answer