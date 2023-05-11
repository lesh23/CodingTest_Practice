# 최댓값과 최솟값
def solution(s):
    # w = [int(x) for x in s.split(" ")]
    # ww = str(min([int(x) for x in s.split(" ")]))+" "+str(max([int(x) for x in s.split(" ")]))
    # print(ww, type(ww))
    # # answer = str(min(s))+" "+str(max(s))
    # # print(answer)
    # answer = ''
    return str(min([int(x) for x in s.split(" ")]))+" "+str(max([int(x) for x in s.split(" ")]))

# JadenCase 문자열 만들기
def solution(s):
    index = [0]
    answer = ''
    for i, j in enumerate(s):
        if j==" ":
            index.append(i+1)
        
    for i, j in enumerate(s):
        if i in index:
            answer = answer + j.upper()
        else:
            answer = answer + j.lower()
            
    return answer

# 최솟값 만들기
def solution(A,B):    
    A.sort()
    B.sort(reverse=True)
    
    # answer = 0
    # for i in range(len(A)):
    #     answer = answer + (A[i] * B[i])
    # return answer
    
    answer = lambda x, y: sum(x[i]*y[i] for i in range(len(x)))
    return answer(A,B)
