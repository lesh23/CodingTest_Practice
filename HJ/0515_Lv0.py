# 양꼬치
def solution(n, k):
    free = len([x for x in range(n+1) if x!=0 and x%10==0])
    answer = n*12000 + ((k-free)*2000)
    return answer

# n의 배수
def solution(num, n):
    answer = lambda x, y: 1 if num%n==0 else 0
    return answer(num,n) 

# 정수 부분
def solution(flo):
    return int(flo)

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 문자열로 변환
def solution(n):
    return str(n)