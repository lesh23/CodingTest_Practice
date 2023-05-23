# 예상 대진표

# 점프와 순간 이동
# 효율성 싪패 ㅠㅠㅠ
def solution(n):
    # ans = 0
    # 일단 1칸 가서
    # 냅다 순간이동만 하고 (2)
    # 홀수일 때 +1 해야 처리된다?
    ans = 1
    while n!=1:
        print(n)
        if n%2==0: # 순간이동맨
            n=n/2
        else: # 홀수면 건전지 써~
            # print('odd')
            n-=1
            ans+=1
    return ans

# N개의 최소공배수
from math import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for i in range(len(arr)-1):
        answer = lcm(answer, arr[i+1])
    return answer