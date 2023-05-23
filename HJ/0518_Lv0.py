# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    x = lambda a,b,f: a+b if flag==True else a-b
    return x(a,b,flag)

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    else: return 0

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    c = lambda arr, k: [a+k for a in arr] if k%2==0 else [a*k for a in arr] 
    return c(arr,k)

# 배열 두 배 만들기
def solution(numbers):
    answer = [x*2 for x in numbers]
    return answer

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k