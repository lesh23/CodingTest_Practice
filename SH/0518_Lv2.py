# 예상 대진표

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