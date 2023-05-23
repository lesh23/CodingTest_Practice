# 멀리 뛰기

# 귤 고르기
# 시간 초과
def solution(k, tangerine):
    answer = 0
    uni = list(set(tangerine))
    count = []
    for i in uni:
        count.append(tangerine.count(i))
    
    count = sorted(count)[::-1]
    # print(uni, count, k)
    tmp=0
    if count[0] >= k:
        return 1
    else:
        for i in count:
            if tmp < k:
                tmp += i
                answer += 1
            else:
                break
    return answer

# 괄호 회전하기