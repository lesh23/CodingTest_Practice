# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = 0
    if n%slice ==0:
        answer = n//slice
    else:
        answer = n//slice +1
    return answer

# 피자 나눠 먹기 (1)
def solution(n):
    answer = 0
    if n%7==0:
        answer = n//7
    else : 
        answer = n//7+1
    return answer

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer >n:
            break
    return answer