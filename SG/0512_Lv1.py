# 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==1:
            return i

# 평균 구하기
def solution(arr):
    answer = 0
    for i in arr:
        answer += float(i)
    return answer/len(arr)

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range (1,n+1):
        answer.append (x*i)
    return answer