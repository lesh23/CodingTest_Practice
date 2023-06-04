### 5/11
# 약수의 합
def solution(n):
    answer = 0
    if n == 0:
        pass
    else :
        for i in range(1,n+1):
            if n % i == 0:
                answer += i
    return answer

# 짝수와 홀수
def solution(num):
    answer = 'Odd'
    if num % 2 == 0:
        answer = 'Even'
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    l = list(str(n))
    for i in l :
        answer += int(i)
    return answer

    # map 이용
    def solution(n):
        return sum(list(map(int, str(n))))

    # 나머지 이용
    def solution(n):
    answer=0
    while n>0:
        answer += n % 10
        n = n // 10
    return answer



### 5/12
# 나머지가 1이 되는 수 찾기
def solution(n):
    if n % 2 == 1 :
        return 2
    else :
        for i in range(3,n):
            if n % i == 1:
                return i

    # 궁금증 : for문에 break 안걸어도 되나, return이 있음으로 전체 함수가 끝?

# 평균 구하기
def solution(arr):
    result =  sum(arr)/len(arr)
    return result

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(n) :
        answer.append(x*(i+1))
    return answer



### 5/15
# 문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    if s.count('p') != s.count('y'):
        return False
    return True

# 자연수 뒤집어 배열로 만들기
def solution(n):
    return list(reversed(list(map(int, str(n)))))

# 정수 제곱근 판별
def solution(n):
    a = n ** (1/2)
    if int(a)**2 == n:
        return (a+1)**2
    return -1



### 5월 17일
# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    a = sorted(list(str(n)), reverse = True)
    return int(''.join(a))

# 하샤드 수
def solution(x):
    
    if x % sum(map(int, str(x))) == 0:
        return True
    
    return False



### 5월 18월
# 두 정수 사이의 합
def solution(a, b):
    if a>b:
        a, b= b,a
    return sum(i for i in range(a,b+1))


# 콜라츠 추측
def solution(num):
    answer = 0
    while num > 1 and answer < 500:
        if num % 2 == 0:
            num /= 2
            answer += 1
        else :
            num = 3*num +1
            answer += 1

    if answer >=500:
        return -1

    return answer


# 서울에서 김서방 찾기
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i].find('Kim') != -1:
            return f'김서방은 {i}에 있다'



### 5월 19일
# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    if answer == [] :
        return [-1]
    return answer

# 핸드폰 번호 가리기
def solution(phone_number):
    answer = '*'*len(phone_number[:-4])+phone_number[-4:]
    return answer

# 정규식 이용방법 생각해보기

# 음양 더하기
def solution(absolutes, signs):
    sign = [1 if x == True else -1 for x in signs]
    return sum(absolutes[i]*sign[i] for i in range(len(sign)))
    


### 5월 22일
# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# 제일 작은 수 제거하기
def solution(arr):
    arr.pop(arr.index(min(arr)))
    
    if len(arr) == 0:
        arr=[-1]
    return arr

# 가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else :
        return s[len(s)//2-1:len(s)//2+1]
    


### 5월 24일
# 수박수박수박수박수박수?
def solution(n):
    a = '수'
    b = '수박'
    if n %2 == 0:
        return b*(n//2)
    else:
        return b*(n//2)+a
    
# 내적
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''.join(sorted(s))
    return answer[::-1]



# 5월 25일 
# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left, right+1):
        for j in range(1,i+1):
            if i%j==0:
                cnt += 1
                
        if cnt % 2== 0:
            answer += i
        else:
            answer -= i
        
        cnt =0
    return answer
# 다른 사람 풀이 - 제곱수는 약수의 개수가 홀수

# 부족한 금액 계산하기
def solution(price, money, count):
    if price * sum([x for x in range(count+1)]) - money >=0 :
        return price * sum([x for x in range(count+1)]) - money
    else :
        return 0
    
# 문자열 다루기 기본
def solution(s):
    if len(s)== 4 or len(s)== 6:
        return s.isdigit()
    return False



# 5월 26일
# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    arr = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr.append(arr1[i][j]+arr2[i][j])
        answer.append(arr)
        arr=[]
    return answer
# 다른 사람 풀이 - zip / 코드 더 간결하게 하는 방법

# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))

s = '*'*a
for j in range(b):
    print(s)

# 최대공약수와 최소공배수
import math
def solution(n, m):
    return [math.gcd(n,m), n*m/math.gcd(n,m)]



# 5월 29일
# 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1,(len(arr))):
        
        if arr[i] == arr[i-1]:
            continue
        else :
            answer.append(arr[i])

    return answer

# 3진법 뒤집기
def solution(n):
    arr = []
    while n > 2:
        arr.append(n % 3)
        n = n//3

    arr.append(n)

    for i in range(len(arr)) :
        arr[i] = arr[i]*(3**(len(arr)-i-1))
    return sum(arr)

# 이상한 문자 만들기
def solution(s):
    l = s.split(' ')

    for j in range(len(l)):
        a = list(l[j])
        for i in range(len(a)):
            if i%2 ==0:
                a[i] =a[i].upper()
            else :
                a[i] =a[i].lower()

        l[j] = ''.join(a)
        
    return ' '.join(l)



# 5월 31일
# 예산
def solution(d, budget):
    d.sort()
    for i in range(1,len(d)+1):
        # 앞에서부터 부서별 예산 더해서 예산 뛰어넘는 순간 그 전 i 반환
        if sum(d[:i])>budget:
            return i-1
        # 같은 경우는 i반환
        elif sum(d[:i]) == budget:
            return i
    # d 전체 더했는데도 예산보다 작으면 d길이 반환
    return len(d)

# 시저 암호
def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        # 공백은 공백으로
        if s[i] == ' ':
            continue

        # 소문자일 때 밀기
        if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
            if ord(s[i]) + n > ord('z') :
                s[i] = chr((ord(s[i]) + n)-26)
            else :
                s[i] = chr(ord(s[i]) + n)

        # 대문자
        if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
            if ord(s[i]) + n > ord('Z') :
                s[i] = chr((ord(s[i]) + n)-26)
            else :
                s[i] = chr(ord(s[i]) + n)
    
    return ''.join(s)

# 삼총사
from itertools import combinations

def solution(number):
    l = list(combinations(number,3))
    
    answer = 0
    for j in l:
        if sum(j) == 0 :
            answer += 1
    return answer

# 6월 1일
# 최소직사각형
def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = [min(sizes[i]),max(sizes[i])]
    
    return max(sizes[i][0] for i in range(len(sizes)))*max(sizes[i][1] for i in range(len(sizes)))

# [1차] 비밀지도
def solution(n, arr1, arr2):
    zero = '0'*n
    answer = []

    for i in range(n):
        # arr1과 arr2의 각 원소들을 이진수로 바꾸고 앞자리 0으로 메꾸기
        a1 = zero[0:n-len(bin(arr1[i])[2:])] + bin(arr1[i])[2:]
        a2 = zero[0:n-len(bin(arr2[i])[2:])] + bin(arr2[i])[2:]
        a = ''
        # 원소 비교해서 # 또는 공백으로 처리
        for i in range(n):
            if a1[i] == a2[i] and a1[i] == '0':
                a += ' '
            else:
                a += '#'
        # 결과 answer에 append
        answer.append(a)
        
    return answer

# 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer



# 6월 2일
# 숫자 문자열과 영단어	
def solution(s):
    s = s.replace('zero','0')
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five','5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    return int(s)

    # dic, enumerate 이용하는거 확인

# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    # case2 처리해주기 위해서 우선 사전순 배열
    strings.sort()
    return sorted(strings, key=lambda x : x[n])

# K번째수
def solution(array, commands):
    answer = []
    for i in commands :
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer



# 6월 7일
# 두 개 뽑아서 더하기
# 콜라 문제
# 푸드 파이트 대회

# 6월 8일
# 가장 가까운 같은 글자
# 2016년
# 추억 점수

# 6월 6일
# 폰켓몬
# 모의고사
# 명예의 전당 (1)

# 소수 만들기
# 소수 찾기
# 과일 장수

# 실패율
# 카드 뭉치
# [1차] 다트 게임

# 덧칠하기
# 기사단원의 무기
# 로또의 최고 순위와 최저 순위

# 숫자 짝꿍
# 체육복
# 옹알이 (2)

# 완주하지 못한 선수
# 문자열 나누기
# 크레인 인형뽑기 게임

# 키패드 누르기
# 신규 아이디 추천
# 둘만의 암호

# 대충 만든 자판
# 햄버거 만들기
# 성격 유형 검사하기

# 달리기 경주
# 개인정보 수집 유효기간
# 바탕화면 정리

# 신고 결과 받기
# 공원 산책