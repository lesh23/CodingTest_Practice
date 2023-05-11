# 약수의 합
def solution(n):
    answer = 0
    if n == 0:
        pass
    else :
        for i in range(1,n+1):
            if n % i == 0:
                answer += i
    return answer

# 짝수와 홀수
def solution(num):
    answer = 'Odd'
    if num % 2 == 0:
        answer = 'Even'
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    l = list(str(n))
    for i in l :
        answer += int(i)
    return answer

    # map 이용
    def solution(n):
        return sum(list(map(int, str(n))))

    # 나머지 이용
    def solution(n):
    answer=0
    while n>0:
        answer += n % 10
        n = n // 10
    return answer
    