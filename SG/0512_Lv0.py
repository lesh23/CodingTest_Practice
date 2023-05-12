# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

# 각도기
def solution(angle):
    answer = 0
    if 0<angle<90:
        answer = 1
    if angle == 90:
        answer =2
    if 90<angle<180:
        answer=3
    if angle == 180:
        answer=4
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2==0:
            answer +=i    
    return answer

# 배열의 평균 값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer+=i       
    return answer/len(numbers)