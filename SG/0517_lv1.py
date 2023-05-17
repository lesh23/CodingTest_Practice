# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    l = list(str(n))
    for i in range(0,len(l)):
        l[i] = str(l[i])
    l.sort(reverse=True)
    return "".join(map(str, l))

# 하샤드 수
def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x%sum == 0:
        return True
    else:
        return False