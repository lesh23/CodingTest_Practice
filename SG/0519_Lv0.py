# 문자열의 뒤의 n글자
def solution(my_string, n):
    l=list(my_string)
    result=''.join(map(str,l[len(l)-n:len(l)]))
    return result

# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]   
    return answer

# 점의 위치 구하기
def solution(dot):
    answer = 0
    if dot[0]>0 and dot[1]>0:
        answer = 1
    if dot[0]<0 and dot[1]>0:
        answer = 2
    if dot[0]<0 and dot[1]<0:
        answer = 3
    if dot[0]>0 and dot[1]<0:
        answer = 4
    return answer

# 편지
def solution(message):
    answer = 0
    a=list(message)
    answer = len(a)*2
    return answer