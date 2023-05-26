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
# 내적
# 문자열 내림차순으로 배치하기

'''0525'''
# 약수의 개수와 덧셈
# 부족한 금액 계산하기
# 문자열 다루기 기본

'''0526'''
# 행렬의 덧셈
# 직사각형 별찍기
# 최대공약수와 최소공배수

'''0529'''
# 같은 숫자는 싫어
# 3진법 뒤집기
# 이상한 문자 만들기

'''0530'''
# 예산
# 시저 암호
# 삼총사

'''0531'''
# 최소직사각형
# [1차] 비밀지도
# 크기가 작은 부분 문자열
