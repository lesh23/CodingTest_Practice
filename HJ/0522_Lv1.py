# 없는 숫자 더하기
def solution(numbers):
    check=[0,1,2,3,4,5,6,7,8,9]
    return sum([x for x in check if x not in numbers])

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        m = min(arr)
        answer = [x for x in arr if x!=m]
        return answer

# 가운데 글자 가져오기
from math import floor
def solution(s):
    # answer = ''
    if len(s)%2==0:
        return s[(floor(len(s)/2)-1)]+s[(floor(len(s)/2))]
    else:
        return (s[(floor(len(s)/2))])