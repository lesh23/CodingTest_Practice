# 문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    if s.count('p') != s.count('y'):
        return False
    return True

# 자연수 뒤집어 배열로 만들기
def solution(n):
    return list(reversed(list(map(int, str(n)))))

# 정수 제곱근 판별
def solution(n):
    a = n ** (1/2)
    if int(a)**2 == n:
        return (a+1)**2
    return -1