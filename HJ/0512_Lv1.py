# 나머지가 1이 되는 수 찾기
def solution(n):
    # answer = 0
    # for x in range(n+1):
    #     if x!=0 and n%x==1:
    #         answer = x
    #         break
    # return answer

    tmp = [x for x in range(n+1) if x!=0 and n%x==1]
    return tmp[0]

# 평균 구하기
def solution(arr):
    return sum(x for x in arr)/len(arr)

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer =  [x]
    for i in range(n-1):
        answer.append(answer[i]+x)
    return answer