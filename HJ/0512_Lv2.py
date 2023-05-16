# 올바른 괄호
def solution(s):
    score = 0
    answer = True
    for p in s:
        if not score < 0:
            if p == '(':
                score+=1
            elif p == ')':
                score-=1
        elif score < 0 : answer = False
    if score !=0 : answer = False
    
    return answer

# 이진 변환 만들기
def solution(s):
    answer = []
    count = 0 #회차
    ztr = 0 # zeros to remove
    larz = 0 # length after removing zero
    while larz != 1:
        ztr += s.count("0") # 지운 0 누적
        # s = s.replace("0", "") # 0을 뺀 문자열 갱신
        # larz = len(s) # 0을 뺀 새로운 문자열 길이
        larz = s.count("1")
        count +=1 # 한 번의 회차가 끝났다는 것
        s = bin(larz)[2:] # 길이를 이진법으로 다시 표현
        # 1이 될 때까지 while문에서 반복
        
    answer = [count, ztr]
    return answer

# 숫자의 표현
# def solution(n):
#     answer = 0
#     numbers = [x for x in range(n+1)]
#     for i in numbers:
#         sum = 0
#         rnd = numbers[i+1:]
#         for x in rnd:
#             if sum<15:
#                 if len(rnd)==1: 
#                     answer+=1
#                 else:
#                     sum+=x
#             elif sum>15:
#                 break
#             elif sum==15:
#                 answer+=1
#                 break
#     return answer