# 없는 숫자 더하기
def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]    
    return sum(set(arr)-set(numbers))

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
    if len(arr) ==1:
        arr=[-1]
    return arr

# 가운데 글자 가져오기
def solution(s):
    answer = ''
    a=len(s)
    if a%2==1:
        answer = s[a//2]
    else:
        answer = s[a//2-1] +s[a//2]
    return answer