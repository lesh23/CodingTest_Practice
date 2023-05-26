'''0511'''
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

'''0512'''
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

'''0515'''
# 다음 큰 숫자
def solution(n):
    # 1의 개수 구하기
    ones= len([x for x in bin(n)[2:] if x == '1'])
    # answer = 0

    # n++ 반복. 1의 개수가 맞을 때 까지 (효율 똥일듯)
    while True:
        n+=1
        tmp = len([y for y in bin(n)[2:] if y=='1'])
        if ones == tmp:
            return n
        else:
            continue
        

# 피보나치 수
def solution(n):
    num = fib(n)
    if num!=0:
        answer = num%1234567
    return answer

def fib(x):
    if x<2: return x
    elif x<0: return 0
    else:
        return (fib(x-1)+(fib(x-2)))
    
# def solution(n):
#     for i in reversed(range(n+1)):
#         print(i)

# 짝지어 제거하기
def solution(s):
    tmp=[]
    
    for i in s: 
        if len(tmp)==0:
            tmp.append(i)
        else:
            if i == tmp[-1]:
                tmp.pop()
            else:
                tmp.append(i)
                
    if len(tmp)==0: return 1
    else: return 0

'''0517'''
# 영어 끝말잇기
def solution(n, words):
    game=[]
    rnd=0
    person= lambda x: n if (x+1)%n==0 else (x+1)%n
    for i,w in enumerate(words):
        if i%n==0:
            rnd+=1
        if w in game:
            return [person(i), rnd]
        else:
            if game!=[]:
                game.append(w)
                if game[i-1][-1]!=w[0]:
                    return [person(i), rnd]
                else:
                    continue
            else:
                game.append(w)
    return [0,0]


# 카펫


# 구명보트
# 효율성 에러,,;;
def solution(people, limit):
    answer = 0
    ppl = sorted([x for x in people])
    while ppl:
        # print(ppl, ppl[0], ppl[-1])
        if ppl[0] + ppl[-1] <= limit:
            ppl.pop()
            ppl=ppl[1:]
        else:
            ppl.pop()
        answer+=1
    return answer

'''0518'''
# 예상 대진표

# 점프와 순간 이동
# 효율성 싪패 ㅠㅠㅠ
def solution(n):
    # ans = 0
    # 일단 1칸 가서
    # 냅다 순간이동만 하고 (2)
    # 홀수일 때 +1 해야 처리된다?
    ans = 1
    while n!=1:
        print(n)
        if n%2==0: # 순간이동맨
            n=n/2
        else: # 홀수면 건전지 써~
            # print('odd')
            n-=1
            ans+=1
    return ans

# N개의 최소공배수
from math import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for i in range(len(arr)-1):
        answer = lcm(answer, arr[i+1])
    return answer

'''0519'''
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

'''0522'''
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

'''0524'''
# 행렬의 곱셈

'''0525'''
# n^2 배열 자르기

'''0526'''
# 의상

'''0529'''
# 튜플

'''0530'''
# 기능개발

'''0531'''
# 프로세스x