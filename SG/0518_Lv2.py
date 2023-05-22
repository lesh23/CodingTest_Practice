# 예상 대진표
def solution(n,a,b):
    answer = 0
    while a != b :
        if a%2 == 1:
            a = a//2+1
        else:
            a = a//2
        if b%2==1:
            b = b//2+1
        else:
            b = b//2
        answer += 1
    return answer

# 점프와 순간 이동 - while문
def solution(n):
    cnt = 0
    while n != 0:
        if n%2==0:
            n = n/2
        else:
            n -= 1
            cnt += 1
    return cnt

# 점프와 순간 이동 - while문의 원리가 2진수 바꾸는 법
def solution(n):
    return bin(n).count('1')

# N개의 최소공배수
def solution(arr):
    def lcm(a, b):
        for i in range(max(a, b), (a * b) + 1):
            if i % a == 0 and i % b == 0:
                return i
    for j in range(0,len(arr)-1):              # 앞에서 두 개씩 최소공배수 구하기
        arr[j+1] = lcm(arr[j],arr[j+1])
    return(arr[-1])