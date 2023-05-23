# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
    
# 점의 위치 구하기
def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            return 1
        else: return 4
    else:
        if dot[-1]>0:
            return 2
        else: return 3

# 편지
def solution(message):
    return len(message)*2