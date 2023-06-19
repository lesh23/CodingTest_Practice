### 5/11
# 최댓값과 최솟값
def solution(s):
    l = list(map(int, s.split(' ')))
    answer = str(min(l)) + str(' ') +str(max(l))
    return answer

# JadenCase 문자열 만들기
def solution(s):
    # 전부 다 소문자로 만들고
    l=s.lower().split(' ')

    for i in range(len(l)):
        # 맨 앞글자 대문자로 만들고 그 뒤에 나머지꺼 합체
        if len(l[i]) >= 2:
            l[i] = l[i][0].upper() + l[i][1:] 

         # 연속된 공백이라는 문제 조건 고려 & 한글자짜리 고려
        else :
            l[i] = l[i].upper()

    # 공백으로 join        
    return ' '.join(l)

    # 파이썬 내장 함수 이용
    def solution(s):
        return s.title()

# 최솟값 만들기
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]    
    return answer



### 5/12
# 올바른 괄호
def solution(s):
    s = list(s)
    l=0 # 괄호 짝꿍 찾는 변수
    l_c, r_c=0,0 # 각 괄호 개수
    re = []
    
    for i in range(len(s)):
        # (괄호는 +1 , )괄호는 -1로 계산

        if s[i] == '(':
            l += 1
            l_c += 1
            re.append(l)              
        else :
            l -= 1
            r_c +=1
            re.append(l)  

    # 시작이 ) 이거나, 괄호 총 개수가 홀수거나, )괄호 개수가 (괄호보다 많거나, 괄호 짝꿍이 안맞거나
    if re[0] < 0 or len(s)%2==1 or re.count(-1)>0 or l_c != r_c:
        return False
    else:
        return True


# 이진 변환 만들기
def solution(s):
    cnt, zero_cnt =0,0

    while s != '1':
        cnt += 1
        l = s.count('1')
        zero_cnt += s.count('0')
        s = bin(l)[2:]
        
    return [cnt, zero_cnt]


# 숫자의 표현
def solution(n):
    answer = 0
    # 연속하는 수 방정식 계산하는 방법으로 생각
    # x+(x+1)+(x+2) = 15 를 예로 들면 3x + (1+2) = 15가 됨
    # 3x = 15 - (1+2)가 됨으로 for문을 이용해서 ix + (i-1)i/2 = n 이라는 방정식을 해결한다고 생각하고 접근
    for i in range(1,n+1):
        if n-(i-1)*i/2 > 0 :
            if (n-(i-1)*i/2) % i == 0:
                answer += 1
        else :
            break
        
    return answer



### 5/15
# 다음 큰 숫자
def solution(n):
    a = bin(n)[2:]
    c = a.count('1')
    
    while True:
        n = n+1
        b = bin(n)[2:].count('1')
        
        if b==c :
            return n
            break

# 피보나치 수
# for문 + 메모리제이션
def solution(n):
    d = [0]*100001
    d[1],d[2] = 1,1
    for i in range(2,n+1) :
        d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567

# 피보나치 코드 재귀함수 - 런타임에러+시간초과
def fibo(n):
    if n==1 or n==2 :
        return 1
    return fibo(n-1) + fibo(n-2)

def solution(n):
    return fibo(n) % 1234567

# 재귀함수 + 메모리제이션 - 런타임에러
def fibo(n):
    d=[0]*100001
    if n==1 or n==2 :
        return 1
    if d[n] != 0:
        return d[n] 
    
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n] 

def solution(n):
    return fibo(n) % 1234567


# 짝지어 제거하기
# 정확성: 30.3 / 효율성: 0.0 / 합계: 30.3 / 100.0
def solution(s):
    s= list(s)
    answer = 1
    
    if len(s) % 2 ==  1:
        answer = 0

    else :
        while answer == 1 and len(s) > 0 :
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    answer = 1
                    break
                else:
                    answer = 0
    return answer


# 정확성: 40.3 / 효율성: 19.9 / 합계: 60.2 / 100.0 -> 시간 초과
def solution(s):
    s= list(s)
    answer = 1
    d=[0] * 26
    
    if len(s) % 2 ==  1:
        return 0

    for i in range(97,123):
        d[i-97] = s.count(chr(i))
        if d[i-97] % 2 == 1:
            return 0
        
    while answer == 1 and len(s) > 0 :
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                answer = 1
                break
            else:
                answer = 0 
    return answer



### 5/17
# 영어 끝말잇기

# 카펫
def solution(brown, yellow):
    
    l = sorted([x for x in range(1,brown+yellow+1) if (brown+yellow) % x == 0 ], reverse = True)

    for i in l:
        if yellow % (i-2) == 0:
            return [i,(brown+yellow) // i]

# 구명보트
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
     
    for i in people: 
        if i + people[-1] <= limit :
            people.pop(-1)
            answer += 1
        else :
            answer += 1

    return answer

# 첫번째 코드(정확성 : 75/75, 효율성 :0/25)
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0

    while len(people) != 0:
        if len(people) == 1:
            people.pop(0)
            answer+= 1
            break
        
        if people[0] > limit:
            people.pop(0)
            answer += 1
        else :

            if people[0] + people[-1] <=limit:
                people.pop(-1)
                people.pop(0)
                answer += 1
            else :
                people.pop(0)
                answer += 1

    return answer



# 5/18
# 예상 대진표
def solution(n,a,b):
    a, b = min(a,b), max(a,b)
    
    if b-a ==1 and b%2==0:
        return 1
    
    for i in range(2,21):
        if 2**i == n:
            i = i
            break 

    while i > 1:
        if a <= 2**(i-1) and b > 2**(i-1):
            return i

        if a > 2**(i-1):
            a = a - 2**(i-1)
            b = b - 2**(i-1)
            
        i -= 1
        

# 점프와 순간 이동


# N개의 최소공배수
def solution(arr):
    arr.sort()
    answer = arr[0]
    
    for i in range(1,len(arr)):
        for j in range(answer,arr[i]*answer + 1) :
            if j % answer == 0 and j % arr[i] == 0:
                answer = j 
                break
                
    return answer


# 틀림
def solution(arr):
    arr.sort()
    answer = 1
    
    # 최소공배수 구하는 방법으로 접근
    # [5,6,9] 이런 test case 어떻게 하지
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] % arr[i] == 0:
                arr[j] //= arr[i]

    for i in arr:
        answer *= i    
    
    return answer

# 스파이더에서는 돌아가는데 프로그래머스에서는 작동 안함
import math

arr=[2,6,8,14]	
arr.sort()
answer = arr[0]

for i in range(1,len(arr)):
    
    answer = math.lcm(answer, arr[i])

answer



### 5/19
# 멀리 뛰기
def solution(n):
    arr = [0]*(n+1)
    
    if n <=2 :
        return n
    else :
        arr[1], arr[2] = 1, 2
        for i in range(3,n+1):
            arr[i] = (arr[i-1] + arr[i-2])% 1234567
            
    return arr[n]

# 귤 고르기
# 시간초과
def solution(k, tangerine):
    l = []
    answer = 0
    
    for i in set(tangerine):
        l.append(tangerine.count(i))

    l.sort(reverse=True)

    for i in l:
        if k - i <= 0:
            answer += 1
            return answer
        else :
            k -= i
            answer += 1

# 라이브러리 이용
from collections import Counter

def solution(k, tangerine):


    count = Counter(tangerine)
    sorted_values = sorted(count.values(), reverse=True)
    answer = 0

    for i in sorted_values:
        if k - i <= 0:
            answer += 1
            return answer
        else :
            k -= i
            answer += 1 



### 5/22
# H-Index
def solution(citations):
    citations.sort()
    h = min(citations[len(citations) // 2], sum(citations)//len(citations))
    answer = 0

    for i in citations:
        if i >= h:
            answer += 1

    if h <= answer:
        h += 1
        answer = 0
        
        while True:
            for i in citations:
                if i >= h:
                    answer += 1

            if h <= answer:
                h += 1
                answer = 0
            else :
                return h-1
    else:
        h -= 1
        answer = 0
        
        while True:
            for i in citations:
                if i >= h:
                    answer += 1

            if h > answer:
                h -= 1
                answer = 0
            else :
                return h
        

# 연속 부분 수열 합의 개수
def solution(elements):
    # elements 길이 2배로 늘려줌
    elements = elements*2
    l = []
    
    # 그리고 수열합 실행
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            l.append(sum(elements[j:j+i+1]))

    # set으로 중복제거                
    return len(set(l))

# 시간 초과
def solution(elements):
    l = []

    for i in range(len(elements)):
        for j in range(len(elements)):
            l.append(sum(elements[(j+x)%len(elements)] for x in range(i+1)))
            
    return len(set(l))
        
        
# 시간 초과
# 중간까지 계산하고 뒤에 값은 앞의 계산값을 빼준 값임을 이용
def solution(elements):
    l= set(elements)
    
    for i in range(1, len(elements)//2+1):
        for j in range(len(elements)):
            l.add(sum(elements[(j+x)%len(elements)] for x in range(i+1)))
            
    for i in list(l):
        l.add(sum(elements) - i)
    
    l.add(sum(elements))
    
    return len(l)



''' 카드 포인트 문제 '''
members = [['a','-'],['b','a'],['c','b'],['d','b'],['e','-'],['f','d'], ['g','f']]
p = 100

# members를 dic으로 만들기 + answer을 일단 dic으로 만듬
m = {}
answer = {}

for i in members:
    m[i[0]] = i[1]
    answer[i[0]] = 0

# {'a': '-', 'b': 'a', 'c': 'b', 'd': 'b', 'e': '-', 'f': 'd'}
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}

for i in m.keys():
    cnt = 0
    key = i
    while m[key] != '-' :
        answer[m[key]] += int(p * (0.1**cnt))
        key = m[key]
        cnt += 1

l = sorted([[a,b] for a,b in zip(answer.keys(), answer.values())], key=lambda x: x[1],reverse = True)



### 6/7
# 괄호 회전하기
def solution(s):
    cnt=0
    
    # 문자열 회전하는 for문
    for _ in range(len(s)):
        stack = []
        num = 0
        # 문자열 안에 원소 하나씩 확인
        for i in s:
            if i == '[' or i == '{' or i == '(' :
                stack.append(i)
                num += 1
            else : 
                if stack == [] :
                    break
                elif i == ']' and '[' in stack :
                    stack.pop()
                    num += 1
                elif i == '}' and '{' in stack :
                    stack.pop()
                    num += 1
                elif i == ')' and '(' in stack :
                    stack.pop()
                    num += 1
        
        # for문이 몇번 돌아갔는지 세서 길이랑 비교 & 13번 케이스 걸러내가 위한 조건 추가
        if num == len(s) and stack == []:
            cnt += 1

        s= s[1:]+s[0]
        
    return cnt



### 6/8
# [1차] 캐시



### 6/9
# 행렬의 곱셈



### 6/12
# n^2 배열 자르기



### 6/13
# 의상

### 6/14
# 튜플


### 6/15
# 기능개발


### 6/16
# 프로세스

# [1차] 뉴스 클러스터링
# 할인 행사
# 피로도

# 타겟 넘버
# 전화번호 목록
# k진수에서 소수 개수 구하기

# [3차] 압축
# [3차] n진수 게임
# 더 맵게

# 주차 요금 계산
# 오픈채팅방
# 주식가격

# 땅따먹기
# 게임 맵 최단거리
# 방문 길이

# 스킬트리
# 모음사전
# [3차] 파일명 정렬

# [1차] 프렌즈4블록
# 뒤에 있는 큰 수 찾기
# 2 x n 타일링

# 2개 이하로 다른 비트
# 숫자 변환하기
# 다리를 지나는 트럭

# 롤케이크 자르기
# 가장 큰 수
# 소수 찾기

# 쿼드압축 후 개수 세기
# 큰 수 만들기
# 삼각 달팽이

# 124 나라의 숫자
# 택배상자
# 메뉴 리뉴얼

# 두 큐 합 같게 만들기
# 연속된 부분 수열의 합
# 괄호 변환

# [3차] 방금그곡
# 수식 최대화
# 행렬 테두리 회전하기

# 무인도 여행
# 전력망을 둘로 나누기
# 줄 서는 방법
# 배달
# 가장 큰 정사각형 찾기
# 거리두기 확인하기
# 점 찍기
# 멀쩡한 사각형
# 호텔 대실
# 마법의 엘리베이터
# 문자열 압축
# 숫자 카드 나누기
# 하노이의 탑
# 혼자 놀기의 달인

# 후보키
# 테이블 해시 함수
# 미로 탈출
# 시소 짝꿍
# 광물 캐기
# 디펜스 게임
# N-Queen
# 우박수열 정적분
# 조이스틱
# 리코쳇 로봇
# 두 원 사이의 정수 쌍
# 숫자 블록
# 요격 시스템
# 순위 검색
# 혼자서 하는 틱택토
# 이모티콘 할인행사
# 양궁대회
# 3 x n 타일링
# 과제 진행하기
# 교점에 별 만들기
