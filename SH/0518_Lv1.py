# 두 정수 사이의 합
def solution(a, b):
    if a>b:
        a, b= b,a
    return sum(i for i in range(a,b+1))


# 콜라츠 추측
def solution(num):
    answer = 0
    while num > 1 and answer < 500:
        if num % 2 == 0:
            num /= 2
            answer += 1
        else :
            num = 3*num +1
            answer += 1

    if answer >=500:
        return -1

    return answer


# 서울에서 김서방 찾기
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i].find('Kim') != -1:
            return f'김서방은 {i}에 있다'