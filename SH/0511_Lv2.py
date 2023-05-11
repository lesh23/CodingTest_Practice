# 최댓값과 최솟값
def solution(s):
    l = list(map(int, s.split(' ')))
    answer = str(min(l)) + str(' ') +str(max(l))
    return answer

# JadenCase 문자열 만들기
def solution(s):
    l=s.lower().split(' ')
    for i in range(len(l)):
        if len(l[i]) >= 2:
            l[i] = l[i][0].upper() + l[i][1:] 
        else :
            l[i] = l[i].upper()
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