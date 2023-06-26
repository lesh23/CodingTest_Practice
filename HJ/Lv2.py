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
def solution(s):
    answer = len(s)
    match={'(':')', '[':']', '{':'}' }
    for i in range(len(s)):
        tmp=[]
        # print(s)
        for i, p in enumerate(s):
            # 첫 괄호가 닫힘 괄호면 break
            if i==0 and p in match.values():
                # print('First is closing p', p, answer)
                answer-=1
                break
                
            # 다음 읽는 괄호가 닫힘 괄호가 아니면, tmp에 넣자
            elif p in match.keys():
                # print('Appending open p', p)
                tmp.append(p)
                # print('tmp is ', tmp)
                
            # 다음 읽는 괄호가 닫힘 괄호면, tmp마지막에 들어간거랑 짝이면 pop
            elif p in match.values():
                # print('p is closing', p)
                # if tmp is already empty, but a new closing is read
                if len(tmp)==0:
                    # print('there are no existing open p to pair with', answer)
                    answer-=1
                    break
                # if p not in tmp? break
                elif p not in [match[t] for t in tmp]:
                    # print('p pair doesn\'t exist in tmp', answer)
                    answer-=1
                    break
                elif p==match[tmp[-1]]:
                    # print('closing matching last open in tmp! popping', tmp[-1],'!')
                    # print(p, tmp, match[tmp[-1]])
                    tmp.pop()
                else:
                    answer-=1
                    break
                    
            # 마지막 까지 읽었는데 tmp가 아직 풀일 때
            if i==len(s)-1 and len(tmp)!=0:
                # print('tmp is still not empty!')
                answer-=1
                break
        # if len(tmp)==0:   #### problem: the tmp list starts empty. if nothing happens, it'll still go to this checkpoint making answer++
#         answer+=1
        
        # print('!!!!!!!!!Next string!!!!!!!!!!!')
        s+=s[0]
        s=s[1:]
                
                
            
    return answer

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
def solution(cacheSize, cities):
    answer = 0
    # cities = [x.lower() for x in cities]
    store = []
    for x in [x.lower() for x in cities]:
        if x not in store:
            if len(store)<cacheSize:
                store.append(x)
                answer+=5
            elif cacheSize==0:
                answer+=5
            else:
                store=store[1:]
                store.append(x)
                answer+=5
        elif x in store:
            store.pop(store.index(x))
            store.append(x)
            answer+=1
    return answer

'''0524'''
# 행렬의 곱셈
def solution(arr1, arr2):
    answer = []
    
    n = len(arr1)
    m = len(arr2[0])

    for i in range(n):
        answer.append([0]*m)
        
    for i in range(n):
        for j in range(m):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j] 
    return answer

'''0525'''
# n^2 배열 자르기  time error
def solution(n, left, right):
    answer = []
    ele=[]
    for i in range(n):
        ele.append([i+1]*(i+1))
        if len(ele) < n:
            t=i
            x = n - len(ele)
            while x>0:
                t+=1
                ele[i].append(t+1)
                x-=1        
        
    for a in ele:
        answer+=a
        
    answer = answer[left:right+1]

    return answer

'''0526'''
# 의상
def solution(clothes):
    answer = 1
    gear = {}
    for _,g in clothes:
        gear[g] = 0
        
    for c,g in clothes:
        gear[g] += 1
        
    for v in gear.values():
        answer*=(v+1)
        print(v, answer)
        
    return answer-1

'''0529'''
# 튜플
def solution(s):
    answer = []
    s = s.replace(',{','A')
    s = s.replace('}','')
    s = s.replace('{','')
    s = s.split('A')
    tmp=[]
    for x in s:
        t = []
        for i in x.split(','):
            t.append(int(i))
        tmp.append(t)
    tmp = sorted(tmp, key=len)
    
    for i in tmp:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer

'''0530'''
# 기능개발 실패
def solution(progresses, speeds):
    answer = []
    count=[]
    x=0
    for i,p in enumerate(progresses):
        cnt=0
        while p<100:
            p+=speeds[i]
            cnt+=1
        count.append(cnt)
        if len(count)==1 and cnt==count[-1]:
            x=1
        else:
            if cnt < count[i-1]:
                x+=1
            elif cnt == count[i-1]:
                x+=1
            elif cnt>count[i-1]:
                answer.append(x)
                x=1
            if i == len(progresses)-1:
                answer.append(x)
    return answer

'''0531'''
# 프로세스x