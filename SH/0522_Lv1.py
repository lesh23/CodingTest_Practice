# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# 제일 작은 수 제거하기
def solution(arr):
    arr.pop(arr.index(min(arr)))
    
    if len(arr) == 0:
        arr=[-1]
    return arr

# 가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else :
        return s[len(s)//2-1:len(s)//2+1]