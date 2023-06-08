'''0511'''
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

'''0512'''
# 나머지가 1이 되는 수 찾기
def solution(n):
    # answer = 0
    # for x in range(n+1):
    #     if x!=0 and n%x==1:
    #         answer = x
    #         break
    # return answer

    tmp = [x for x in range(n+1) if x!=0 and n%x==1]
    return tmp[0]

# 평균 구하기
def solution(arr):
    return sum(x for x in arr)/len(arr)

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer =  [x]
    for i in range(n-1):
        answer.append(answer[i]+x)
    return answer

'''0515'''
# 문자열 내 p와 y의 개수
def solution(s):
    a=len([x for x in s.lower() if x =='p'])
    b=len([x for x in s.lower() if x =='y'])
    if a==b: return True
    else: return False

    # return len() == len()
    # return s.count() == s.count()

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = [int(x) for x in reversed(str(n))]
    return answer

# 정수 제곱근 판별
from math import sqrt
def solution(n):
    if n%sqrt(n)==0:
        return (sqrt(n)+1)**2
    else: return -1

'''0517'''
# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    answer = int(''.join(sorted(str(n))[::-1]))
    return answer

# 하샤드 수
def solution(x):
    s = sum([int(i) for i in str(x)])
    answer = lambda x, s: True if x%s==0 else False
    return answer(x,s)

'''0518'''
# 두 정수 사이의 합
def solution(a, b):
    p = lambda x,y: sum([i for i in range(x,y+1)]) if x<y else sum([i for i in range(y,x+1)])
    return p(a,b)

# 콜라츠 추측
def solution(num):
    answer = 0
    if num==1: answer = 0
    elif num>1:
        while num!=1:
            answer+=1
            if num%2==0:
                num=num/2
            else:
                num=(num*3)+1
        if answer>=500:
            answer = -1
                
    return answer

# 서울에서 김서방 찾기
def solution(seoul):
    for i,j in enumerate(seoul):
        if j == 'Kim':
            return "김서방은 "+str(i)+"에 있다"
        
'''0519'''
# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = sorted([x for x in arr if x%divisor==0])
    if answer==[]:
        answer=[-1]
    return answer

# 핸드폰 번호 가리기
def solution(phone_number):
    return phone_number.replace(phone_number[:-4],'*'*len(phone_number[:-4]))

# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for i, j in enumerate(absolutes):
        print(signs[i])
        if signs[i]==True:
            answer+=j
        else: answer-=j
    return answer

'''0522'''
# 없는 숫자 더하기
def solution(numbers):
    check=[0,1,2,3,4,5,6,7,8,9]
    return sum([x for x in check if x not in numbers])

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        m = min(arr)
        answer = [x for x in arr if x!=m]
        return answer

# 가운데 글자 가져오기
from math import floor
def solution(s):
    # answer = ''
    if len(s)%2==0:
        return s[(floor(len(s)/2)-1)]+s[(floor(len(s)/2))]
    else:
        return (s[(floor(len(s)/2))])
    
'''0524'''
# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i%2==0:
            answer += '박'
        else:
            answer += '수'
    return answer

# 내적
def solution(a, b):
    answer = sum([a[i]*b[i] for i,_ in enumerate(a)])
    return answer

# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''.join(sorted(s))[::-1]
    return answer

'''0525'''
# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tmp = yaksu(i)
        if len(tmp)%2==0:
            answer+=i
        else:
            answer-=i
    return answer

def yaksu(n):
    answer = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            answer.append(i)
    answer.append(n)
    return answer

# 부족한 금액 계산하기
def solution(price, money, count):
    total=sum([price*n for n in range(1,count+1)])
    if not total>money:
        return 0
    else:
        return abs(total-money)
    
# 문자열 다루기 기본
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit()==True:
        return True
    else: return False

'''0526'''
# 행렬의 덧셈
def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j]  for j in range
(len(arr1[0]))] for i in range(len(arr1))]
    return answer

# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)

# 최대공약수와 최소공배수

def solution(n, m):
    return [gcd(n,m), lcm(n,m)]


def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


def lcm(x, y):
    if x > y:
        greater = x
    else:       
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


'''0529'''
# 같은 숫자는 싫어
def solution(arr):
    answer = []
    tmp=-1
    for a in arr:
        if a==tmp:
            pass
        else:
            tmp = a
            answer.append(a)
    return answer

# 3진법 뒤집기 응 꺼져

# 이상한 문자 만들기 ㅈ같네 진짜
def solution(s):
    answer = ''
    s=s.split(' ')
    for a in s:
        word=''
        for i, b in enumerate(a):
            if i%2==0:
                word+=b.upper()
            else:
                word+=b.lower()
        
        answer +=''.join(word)
        answer+=' '
    if answer[-1]==' ':
        answer = answer[:-1]
    return answer

'''0530'''
# 예산  #error
def solution(d, budget):
    answer = 0
    d=sorted(d)[::-1]
    while budget>0:
        if budget>=d[-1]:
            budget-=d[-1]
            d.pop()
            answer+=1
        else:
            break
    return answer
# 시저 암호
def solution(s, n):
    answer = ''
    for i in s:
        x = ord(i)
        if x>=65 and x<=90:
            if x+n>90:
                answer += chr((x+n)-26)
            else:
                answer += chr(x+n)
        elif x>=97 and x<=122:
            if x+n>122:
                answer += chr((x+n)-26)
            else:
                answer += chr(x+n)
        elif x==32:
            answer += ' '
    return answer

# 삼총사

'''0531'''
# 최소직사각형
# [1차] 비밀지도
# 크기가 작은 부분 문자열


'''0601'''
# 숫자 문자열과 영단어
def solution(s):
    answer = ''
    print(s)
    dic = {'ze': [0,4],'on': [1,3],'tw': [2,3],'th': [3,5],'fo': [4,4],'fi': [5,4],'si': [6,3],'se': [7,5],'ei': [8,5],'ni': [9,4]}
    if s.isdigit():
        return int(s)
    else:
        #"23four5six7"
        for i, x in enumerate(s):
            if x.isdigit():
                answer+=x
            else:
                if i<len(s)-1:
                    tmp = s[i]+s[i+1]
                    if tmp in dic:
                        answer+=str(dic[tmp][0])
    return int(answer)

# 문자열 내 마음대로 정렬하기
# K번째수

'''0602'''
# 두 개 뽑아서 더하기
# 콜라 문제
# 푸드 파이트 대회






members = [['a','-'],['b','a'],['c','b'],['d','b'],['e','-'],['f','d']]
answer = [['b',200],['a',125],['c',100],['f',0]]
dic = {'ze': [0,],'on': [1,],'tw': [2,],'th': [3,],'fo': [4,],'fi': [5,],'si': [6,],'se': [7,],'ei': [8,],'ni': [9,]}