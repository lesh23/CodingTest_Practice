# H-Index
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer = i+1
    return answer

# 연속 부분 수열 합의 개수
def solution(elements):
    answer = []
    two = elements+elements
    for i in range(0,len(elements)):
        for j in range(0,len(elements)+1):
            answer.append(sum(two[i:i+j]))        
    return len(set(answer))-1               # 너무 오래 걸림..


# [1차] 캐시
