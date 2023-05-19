# 멀리 뛰기
def solution(n):
    arr = [0]*(n+1)
    
    if n <=2 :
        return n
    else :
        arr[1], arr[2] = 1, 2
        for i in range(3,n+1):
            arr[i] = (arr[i-1] + arr[i-2])% 1234567
            
    return arr[n]

# 귤 고르기
# 시간초과
def solution(k, tangerine):
    l = []
    answer = 0
    
    for i in set(tangerine):
        l.append(tangerine.count(i))

    l.sort(reverse=True)

    for i in l:
        if k - i <= 0:
            answer += 1
            return answer
        else :
            k -= i
            answer += 1

# 라이브러리 이용
from collections import Counter

def solution(k, tangerine):


    count = Counter(tangerine)
    sorted_values = sorted(count.values(), reverse=True)
    answer = 0

    for i in sorted_values:
        if k - i <= 0:
            answer += 1
            return answer
        else :
            k -= i
            answer += 1 


# 괄호 회전하기