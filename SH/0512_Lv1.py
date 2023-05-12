# 나머지가 1이 되는 수 찾기
def solution(n):
    if n % 2 == 1 :
        return 2
    else :
        for i in range(3,n):
            if n % i == 1:
                return i

    # 궁금증 : for문에 break 안걸어도 되나, return이 있음으로 전체 함수가 끝?

# 평균 구하기
def solution(arr):
    result =  sum(arr)/len(arr)
    return result

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(n) :
        answer.append(x*(i+1))
    return answer