'''0511'''
# 두 수의 곱
def solution(num1, num2):
    return num1 * num2

# 몫 구하기 
def solution(num1, num2):
    return num1%num2

# 두 수의 차
def solution(num1, num2):
    return num1-num2

# 나머지 구하기
def solution(num1, num2):
    return num1//num2

# 나이 출력
def solution(age):
    return (2022 - age)+1

'''0512'''
# 두 수의 합
def solution(num1, num2):
    return num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return int((num1/num2)*1000)

# 각도기
def solution(angle):
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
            
    return answer

    # answer = lambda x: 1 if angle>0 and angle <90 else (2 if angle==90 else (3 if angle > 90 and angle < 180 else 4))
    # return answer(angle)

# 짝수의 합
def solution(n):
    return sum(x for x in range(n+1) if x%2==0)

# 배열의 평균 값
def solution(numbers):
    return sum(x for x in numbers)/len(numbers)

'''0515'''
# 양꼬치
def solution(n, k):
    free = len([x for x in range(n+1) if x!=0 and x%10==0])
    answer = n*12000 + ((k-free)*2000)
    return answer

# n의 배수
def solution(num, n):
    answer = lambda x, y: 1 if x%y==0 else 0
    return answer(num,n) 

# 정수 부분
def solution(flo):
    return int(flo)

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 문자열로 변환
def solution(n):
    return str(n)

'''0517'''
# 숫자 비교하기
def solution(num1, num2):
    answer = lambda x, y: 1 if x==y else -1
    return answer(num1, num2)

# 소문자로 바꾸기
def solution(myString):
    return myString.lower()


# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''.join(arr)
    return answer

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 공배수
def solution(number, n, m):
    answer = lambda i,j,k: 1 if i%j==0 and i%k==0 else 0
    return answer(number, n, m)

'''0518'''
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    x = lambda a,b,f: a+b if flag==True else a-b
    return x(a,b,flag)

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    else: return 0

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    c = lambda arr, k: [a+k for a in arr] if k%2==0 else [a*k for a in arr] 
    return c(arr,k)

# 배열 두 배 만들기
def solution(numbers):
    answer = [x*2 for x in numbers]
    return answer

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k

'''0519'''
# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
    
# 점의 위치 구하기
def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            return 1
        else: return 4
    else:
        if dot[-1]>0:
            return 2
        else: return 3

# 편지
def solution(message):
    return len(message)*2

'''0522'''
# 배열 원소의 길이
def solution(strlist):
    answer = [len(x) for x in strlist]
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

# 피자 나눠 먹기 (3)
from math import ceil

def solution(slice, n):
    return ceil(n/slice)

# 피자 나눠 먹기 (1)
from math import ceil
def solution(n):
    return ceil(n/7)

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for x in numbers: 
        if answer <=n:
            answer+=x
    return answer

'''0524'''
# 중앙값 구하기
def solution(array):
    return sorted(array)[len(array)//2]

# 순서쌍의 개수
def solution(n):
    answer = len([x for x in range(1,n+1) if n%x==0])
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = len([x for x in array if x>height]) 
    return answer

# 중복된 숫자 개수
def solution(array, n):
    answer = len([x for x in array if x==n])
    return answer

# 최댓값 만들기(1)
def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-1]*numbers[-2]

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# 삼각형의 완성조건 (1)
def solution(sides):
    sides = sorted(sides)
    if sides[-1] < sides[0]+sides[1]:
        return 1
    else: return 2

# 문자열 뒤집기
def solution(my_string):
    answer = ''.join(list(my_string)[::-1])
    return answer

# 짝수 홀수 개수
def solution(num_list):
    even, odd = 0,0
    for x in num_list:
        if x%2==0:
            even+=1
        else: odd+=1
    return [even,odd]

# 길이에 따른 연산
from math import prod
def solution(num_list):
    answer = lambda x: sum(i for i in x) if len(x)>=11 else prod(i for i in x)
    return answer(num_list)

'''0525'''
# 옷가게 할인 받기
def solution(price):
    answer = lambda price: price-(price*0.05) if price>=100000 and price<300000 else (price-(price*0.1) if price>=300000 and price<500000 else (price-(price*0.2)) if price>=500000 else price)
    return int(answer(price))

# 아이스 아메리카노
def solution(money):
    cups=0
    while money>=5500:
        money = money - 5500
        cups+=1
    return [cups, money]

# 첫 번째로 나오는 음수
def solution(num_list):
    for i, n in enumerate(num_list):
        if n<0:
            return i
    return -1

# 모음 제거
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for v in vowels:
        if v in my_string:
            my_string = my_string.replace(v,'')
    return my_string

# 원소들의 곱과 합
from math import prod
def solution(num_list):
    answer = lambda num: 1 if prod(num) < sum(num)**2 else 0
    return answer(num_list)

# 정수 찾기
def solution(num_list, n):
    if n in num_list:
        return 1
    else: return 0

# 주사위 게임 1
def solution(a, b):
    if a%2!=0 and b%2!=0:
        return a**2 + b**2
    elif a%2!=0 or b%2!=0:
        return 2*(a+b)
    elif a%2==0 and b%2==0:
        return abs(a-b)
    
# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# 뒤에서 5등 위로
def solution(num_list):
    answer = sorted(num_list)[5:]
    return answer

# 공백으로 구분하기 1
def solution(my_string):
    answer = my_string.split(' ')
    return answer

'''0526'''
# rny_string
def solution(rny_string):
    answer = rny_string.replace('m', 'rn')
    return answer

# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for s in s1:
        if s in s2:
            answer+=1
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer = answer+(s*n)
    return answer

# 자릿수 더하기
def solution(n):
    answer = sum([int(x) for x in str(n)])
    return answer

# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

# 짝수는 싫어요
def solution(n):
    answer = [x for x in range(1,n+1) if x%2!=0]
    return answer

# 카운트 업
def solution(start, end):
    answer = [x for x in range(end+1) if x>=start]
    return answer

# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    else: return 0

# 카운트 다운
def solution(start, end):
    answer = [n for n in range(start+1) if n>=end][::-1]
    return answer

# n개 간격의 원소들
def solution(num_list, n):
    answer = [x for i,x in enumerate(num_list) if i%n==0]
    return answer

'''0529'''
# 문자열 정수의 합
# 숨어있는 숫자의 덧셈 (1)
# 문자열 붙여서 출력하기
# 글자 이어 붙여 문자열 만들기
# 원하는 문자열 찾기
# 배열 만들기 1
# 홀짝 구분하기
# 조건에 맞게 수열 변환하기 1
# 수 조작하기 1
# 뒤에서 5등까지

'''0530'''
# 배열에서 문자열 대소문자 변환하기
# 문자열안에 문자열
# 제곱수 판별하기
# 이어 붙인 수
# 문자열 바꿔서 찾기
# 개미 군단
# 문자열 바꿔서 찾기
# 접두사인지 확인하기
# 더 크게 합치기
# 마지막 두 원소

'''0531'''
# 꼬리 문자열
# 암호 해독
# 가위 바위 보
# 세균 증식
# 홀짝에 따라 다른 값 반환하기
# 대문자와 소문자
# 주사위의 개수
# 공백으로 구분하기 2
# 덧셈식 출력하기
# 배열의 원소만큼 추가하기