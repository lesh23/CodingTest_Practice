# 배열 원소의 길이
def solution(strlist):
    answer = []
    
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    if letter in my_string:
        return my_string.replace(letter,'')
    else:
        return my_string

def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    
    return answer

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = lambda x, y : y // x if y % x == 0 else y//x +1
    return answer(slice, n)

# 피자 나눠 먹기 (1)
def solution(n):

    if n % 7 == 0:
        return n // 7
    
    return n // 7 +1


# n보다 커질 때까지 더하기def solution(numbers, n):
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        
        if answer > n:
            break
    return answer