# H-Index
# 대실패 ㅋㅋ
def solution(citations):
    for x in citations:
        count = 0
        for y in citations:
            if y >= x: 
                count = count+1 
    #             print(x,y,count)
            if len(citations)-count < count:
                # print(x,y,count)
                if y-x < count:
                    answer = count
                    # print("!!", answer)
    return answer


# 연속 부분 수열 합의 개수

# [1차] 캐시