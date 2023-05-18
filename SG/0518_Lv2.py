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

# 점프와 순간 이동

# N개의 최소공배수