# 양꼬치
def solution(n, k):
    answer = (n*12000)+(k*2000)-(n//10)*2000
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    else :
        answer = 0
    return answer

# 정수 부분
def solution(flo):
    answer = 0                  
    import math
    answer = math.floor(flo)
    return answer

# 대문자로 바꾸기
def solution(myString):
    answer = ''
    answer = myString.upper()
    return answer

# 문자열로 변환
def solution(n):
    answer = ''
    answer = str(n)
    return answer