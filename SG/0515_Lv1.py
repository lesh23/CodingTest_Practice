# 문자열 내 p와 y의 개수
def solution(s):
    cnt_p = 0
    cnt_y = 0 
    for i in s:
        if i=='p' or i=='P':
            cnt_p += 1
        if i=='y' or i=='Y':
            cnt_y += 1
    if cnt_p == cnt_y:
        return True
    else:
        return False

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    l = list(map(int, str(n)))
    answer = l[::-1]
    return answer

# 정수 제곱근 판별
def solution(n):
    answer = 0 
    a = n**0.5
    if a == int(a):
        answer = (a+1)**2
    else : 
        answer = -1
    return answer 