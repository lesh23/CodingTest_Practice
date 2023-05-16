# 문자열 내 p와 y의 개수
def solution(s):
    a=len([x for x in s.lower() if x =='p'])
    b=len([x for x in s.lower() if x =='y'])
    if a==b: return True
    else: return False

    # return len() == len()
    # return s.count() == s.count()

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = [int(x) for x in reversed(str(n))]
    return answer

# 정수 제곱근 판별
from math import sqrt
def solution(n):
    if n%sqrt(n)==0:
        return (sqrt(n)+1)**2
    else: return -1