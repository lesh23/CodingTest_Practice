# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    a = sorted(list(str(n)), reverse = True)
    return int(''.join(a))

# 하샤드 수
def solution(x):
    
    if x % sum(map(int, str(x))) == 0:
        return True
    
    return False