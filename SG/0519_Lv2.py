# 멀리 뛰기
def solution(n):
    answer = [1,2]
    for i in range(2,n+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-2]%1234567               # 피보나치..

# 귤 고르기

# 괄호 회전하기