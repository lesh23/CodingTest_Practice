# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a+b
    else :
        return a-b
    
# 부분 문자열
def solution(str1, str2):
    answer = lambda x,y : 1 if y.count(x) !=0 else 0
    return answer(str1, str2)

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 ==1:
        for i in arr:
            answer.append(i*k)
    else :
        for i in arr:
            answer.append(i+k)
    
    return answer

# 배열 두 배 만들기
def solution(numbers):
    return [i*2 for i in numbers]

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k