# 다음 큰 숫자
def solution(n):
    cnt = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == cnt:
            return i
        
# 피보나치 수

# 짝지어 제거하기
def solution(s):
    stack = []
    for i in s:
        if stack ==[]:
            stack.append(i)
        else :
            if i == stack[-1]:
                stack.pop()
            else :
                stack.append(i)
    if stack != [] :
        return 0
    else :
        return 1