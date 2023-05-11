# 최댓값과 최솟값
def solution(s):
    a=s.split()                     #.split(): 문자열을 리스트로 변환
    for i in range(len(a)):
        a[i]=int(a[i])                          
    return str(min(a)) + " " + str(max(a))

# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    a = s.split(' ')                  #''안에 공백이 있어야 함
    for i in range(len(a)): 
        a[i]=a[i].capitalize()       #capitalize: 첫번째 문자만 대문자로 변환
    answer=' '.join(a)               #join(): 리스트를 문자로 변환
    return answer

# 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort()                          #sort(): 오름차순 정렬
    B.sort()
    n=len(A)
    for i in range(n):
        answer += A[i]*B[n-i-1]
    return answer