# 약수의 합
def solution(n):
    # answer = 0
    # for i in range(n+1):
    #     if i != 0 and n%i==0:
    #         answer = answer + i
            
    #### 0부터 n까지 정수 ####
    # a = [x for x in range(n+1)]
    # print(a)
    
    #### 0부터 n까지 정수지만 0이 아니고 나머지가 0인 정수 ####
    # b = [y for y in range(n+1) if y!=0 and n%y==0]
    # print(b)
    
    #### ~의 합 ####
    c = sum(y for y in range(n+1) if y!=0 and n%y==0)
    print(c)
    
    return c

# 짝수와 홀수
def solution(num):
#     if num%2 == 0:
#         answer = "Even"
#     else: answer = "Odd"
    
    answer = lambda x: "Even" if x%2==0 else "Odd"
    return answer(num)

# 자릿수 더하기
def solution(n):
    # type casting?
    # answer = 0
    # for i,j in enumerate(str(n)):
    #     answer = answer + int(j)

    answer = sum(int(y) for x,y in enumerate(str(n)))
    
    return answer