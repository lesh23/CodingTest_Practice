# 약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer +=i
    return answer

# 짝수와 홀수
def solution(num):
    answer = ''
    if num%2==0:
        answer='Even'
    else:
        answer= 'Odd'
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    for i in str(n):
        answer+=int(i)
    return answer