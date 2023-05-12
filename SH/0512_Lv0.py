# 두 수의 합
solution = lambda num1, num2 : num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return (num1*1000) // num2

# 각도기
def solution(angle):
    if angle < 90 :
        answer = 1
    elif angle == 90 :
        answer =2
    elif angle >90 and angle <180:
        answer=3
    else :
        answer=4
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0 :
            answer += i        
    return answer

# 배열의 평균 값
# 라이브러리 사용
import numpy as np
def solution(numbers):
    answer = np.mean(numbers)
    return answer

# 라이브러리 사용 X
def solution(numbers):
    return sum(numbers) / len(numbers)