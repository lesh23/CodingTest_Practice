# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a+b
    else:
        return a-b

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    return 0

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in arr:
            answer.append(i*k)
    else :
        for i in arr:
            answer.append(i+k)
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

# 문자열 곱하기
def solution(my_string, k):
    return (my_string)*k