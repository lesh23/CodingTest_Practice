# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    answer = int(''.join(sorted(str(n))[::-1]))
    return answer

# 하샤드 수
def solution(x):
    s = sum([int(i) for i in str(x)])
    answer = lambda x, s: True if x%s==0 else False
    return answer(x,s)