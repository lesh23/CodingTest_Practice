# 양꼬치
def solution(n, k):
    a = k-(n //10)
    if a <= 0 :
        answer = n*12000
    else :
        answer = n*12000 + a*2000
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num % n ==0:
        answer =1
    return answer

# 정수 부분
def solution(flo):
    answer = int(flo)
    return answer

# 대문자로 바꾸기
def solution(myString):
    answer = myString.upper()
    return answer

# 문자열로 변환
def solution(n):
    return str(n)