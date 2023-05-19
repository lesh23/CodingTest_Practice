# 예상 대진표
def solution(n,a,b):
    a, b = min(a,b), max(a,b)
    
    if b-a ==1 and b%2==0:
        return 1
    
    for i in range(2,21):
        if 2**i == n:
            i = i
            break 

    while i > 1:
        if a <= 2**(i-1) and b > 2**(i-1):
            return i

        if a > 2**(i-1):
            a = a - 2**(i-1)
            b = b - 2**(i-1)
            
        i -= 1
        

# 점프와 순간 이동


# N개의 최소공배수
# 틀림
def solution(arr):
    arr.sort()
    answer = 1
    
    # 최소공배수 구하는 방법으로 접근
    # [5,6,9] 이런 test case 어떻게 하지
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] % arr[i] == 0:
                arr[j] //= arr[i]

    for i in arr:
        answer *= i    
    
    return answer