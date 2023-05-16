# 두 수의 합
def solution(num1, num2):
    return num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return int((num1/num2)*1000)

# 각도기
def solution(angle):
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
            
    return answer

    # answer = lambda x: 1 if angle>0 and angle <90 else (2 if angle==90 else (3 if angle > 90 and angle < 180 else 4))
    # return answer(angle)

# 짝수의 합
def solution(n):
    return sum(x for x in range(n+1) if x%2==0)

# 배열의 평균 값
def solution(numbers):
    return sum(x for x in numbers)/len(numbers)