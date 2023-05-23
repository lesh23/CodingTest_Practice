# 배열 원소의 길이
def solution(strlist):
    answer = [len(x) for x in strlist]
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

# 피자 나눠 먹기 (3)
from math import ceil

def solution(slice, n):
    return ceil(n/slice)

# 피자 나눠 먹기 (1)
from math import ceil
def solution(n):
    return ceil(n/7)

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for x in numbers: 
        if answer <=n:
            answer+=x
    return answer
