# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a<b: 
        for i in range(a,b+1):
            answer += i
    elif b<a:
        for i in range(b,a+1):
            answer +=i
    elif a==b:
        answer = a
    return answer

# 콜라츠 추측
def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer == 500:
            return -1
    return answer

# 서울에서 김서방 찾기
def solution(seoul):   
    for i in range(0,len(seoul)) :
        if seoul[i] == 'Kim':
            return '김서방은 ' + str(i) + '에 있다'