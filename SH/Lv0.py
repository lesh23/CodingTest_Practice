### 5/11
# 두 수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 몫 구하기 
def solution(num1, num2):
    return num1 // num2

# 두 수의 차
def solution(num1, num2):
    return num1-num2

# 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 나이 출력
def solution(age):
    answer = 2022-age+1
    return answer



### 5/12
# 두 수의 합
solution = lambda num1, num2 : num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return (num1*1000) // num2

# 각도기
def solution(angle):
    if angle < 90 :
        answer = 1
    elif angle == 90 :
        answer =2
    elif angle >90 and angle <180:
        answer=3
    else :
        answer=4
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0 :
            answer += i        
    return answer

# 배열의 평균 값
# 라이브러리 사용
import numpy as np
def solution(numbers):
    answer = np.mean(numbers)
    return answer

# 라이브러리 사용 X
def solution(numbers):
    return sum(numbers) / len(numbers)



###5/15
# 양꼬치
def solution(n, k):
    a = k-(n //10)
    if a <= 0 :
        answer = n*12000
    else :
        answer = n*12000 + a*2000
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num % n ==0:
        answer =1
    return answer

# 정수 부분
def solution(flo):
    answer = int(flo)
    return answer

# 대문자로 바꾸기
def solution(myString):
    answer = myString.upper()
    return answer

# 문자열로 변환
def solution(n):
    return str(n)



### 5/17
# 숫자 비교하기
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

# lambda 이용
def solution(num1, num2):
    answer = lambda x,y : 1 if x==y else -1
    return answer(num1,num2)

# 소문자로 바꾸기
def solution(myString):
    return myString.lower()

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    return ''.join(arr)

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 공배수
def solution(number, n, m):
    answer = 0
    if number % n ==0 and number % m ==0:
        answer = 1
    return answer



### 5/18
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a+b
    else :
        return a-b
    
# 부분 문자열
def solution(str1, str2):
    answer = lambda x,y : 1 if y.count(x) !=0 else 0
    return answer(str1, str2)

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 ==1:
        for i in arr:
            answer.append(i*k)
    else :
        for i in arr:
            answer.append(i+k)
    
    return answer

# 배열 두 배 만들기
def solution(numbers):
    return [i*2 for i in numbers]

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k



### 5/19
# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 배열 뒤집기
def solution(num_list):
    return list(reversed(num_list))

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1]>0:
        return 1
    elif dot[0] < 0 and dot[1]>0:
        return 2
    elif dot[0] < 0 and dot[1]<0:
        return 3
    else:
        return 4

# 편지
def solution(message):
    return len(message)*2



### 5/22
# 배열 원소의 길이
def solution(strlist):
    answer = []
    
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    if letter in my_string:
        return my_string.replace(letter,'')
    else:
        return my_string

def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    
    return answer

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = lambda x, y : y // x if y % x == 0 else y//x +1
    return answer(slice, n)

# 피자 나눠 먹기 (1)
def solution(n):

    if n % 7 == 0:
        return n // 7
    
    return n // 7 +1

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        
        if answer > n:
            break
    return answer



### 5/24
# 중앙값 구하기
# 순서쌍의 개수
# 머쓱이보다 키 큰 사람
# 중복된 숫자 개수
# 최댓값 만들기(1)

# # 5/25
# 문자열의 앞의 n글자
# 삼각형의 완성조건 (1)
# 문자열 뒤집기
# 짝수 홀수 개수
# 길이에 따른 연산

# # 5/26
# 옷가게 할인 받기
# 아이스 아메리카노
# 첫 번째로 나오는 음수
# 모음 제거
# 원소들의 곱과 합

# # 5/29
# 정수 찾기
# 주사위 게임 1
# n 번째 원소까지
# 뒤에서 5등 위로
# 공백으로 구분하기 1


# rny_string
# 배열의 유사도
# 문자 반복 출력하기
# 자릿수 더하기
# n 번째 원소부터


# 짝수는 싫어요
# 카운트 업
# 부분 문자열인지 확인하기
# 카운트 다운
# n개 간격의 원소들


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


# 부분 문자열 이어 붙여 문자열 만들기
# 직각삼각형 출력하기
# 문자열 정렬하기 (1)
# 최댓값 만들기 (2)
# 홀수 vs 짝수


# n의 배수 고르기
# 배열의 길이에 따라 다른 연산하기
# 접미사인지 확인하기
# A 강조하기
# 배열 회전시키기


# 인덱스 바꾸기
# 외계행성의 나이
# 가장 큰 수 찾기
# 접미사 배열
# 피자 나눠 먹기 (2)


# 0 떼기
# 문자열 섞기
# 369게임
# 5명씩
# l로 만들기


# 약수 구하기
# 문자열 돌리기
# 배열 비교하기
# 숫자 찾기
# ad 제거하기


# 할 일 목록
# 간단한 식 계산하기
# 콜라츠 수열 만들기
# 배열의 원소 삭제하기
# 문자열 정렬하기 (2)


# 합성수 찾기
# 가까운 1 찾기
# 주사위 게임 2
# 특별한 이차원 배열 2
# 순서 바꾸기


# 9로 나눈 나머지
# 중복된 문자 제거
# 모스부호 (1)
# x 사이의 개수
# 배열 만들기 3


# 팩토리얼
# A로 B 만들기
# 2차원으로 만들기
# 등차수열의 특정한 항만 더하기
# 가까운 수


# 두 수의 연산값 비교하기
# k의 개수
# 진료순서 정하기
# 문자열 잘라서 정렬하기
# 문자열 반복해서 출력하기


# 특별한 이차원 배열 1
# 숨어있는 숫자의 덧셈 (2)
# 한 번만 등장한 문자
# 수 조작하기 2
# 간단한 논리 연산


# 배열 만들기 5
# 수열과 구간 쿼리 3
# 문자열 뒤집기
# 이진수 더하기
# 1로 만들기


# 수열과 구간 쿼리 1
# 세로 읽기
# 컨트롤 제트
# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 소인수분해


# 공 던지기
# 7의 개수
# 날짜 비교하기
# 글자 지우기
# 특수문자 출력하기


# 영어가 싫어요
# 세 개의 구분자
# 잘라서 배열로 저장하기
# 이차원 배열 대각선 순회하기
# 문자열 계산하기


# 문자열 묶기
# 조건에 맞게 수열 변환하기 2
# 문자열이 몇 번 등장하는지 세기
# 빈 배열에 추가, 삭제하기
# 구슬을 나누는 경우의 수


# 삼각형의 완성조건 (2)
# 수열과 구간 쿼리 4
# 리스트 자르기
# 외계어 사전
# qr code


# a와 b 출력하기
# 조건 문자열
# 2의 영역
# 배열의 길이를 2의 거듭제곱으로 만들기
# 커피 심부름


# 문자 개수 세기
# 수열과 구간 쿼리 2
# 캐릭터의 좌표
# 직사각형 넓이 구하기
# 종이 자르기


# 문자열 겹쳐쓰기
# 배열 만들기 4
# 로그인 성공?
# 치킨 쿠폰
# 두 수의 합


# 등수 매기기
# 유한소수 판별하기
# 대소문자 바꿔서 출력하기
# 저주의 숫자 3
# 특이한 정렬


# 문자열 여러 번 뒤집기
# 문자열 밀기
# 정사각형으로 만들기
# 왼쪽 오른쪽
# 그림 확대


# 무작위로 K개의 수 뽑기
# 다항식 더하기
# 배열 만들기 6
# 전국 대회 선발 고사
# 최빈값 구하기


# 배열 만들기 2
# 문자열 출력하기
# OX퀴즈
# 코드 처리하기
# 분수의 덧셈


# 다음에 올 숫자
# 연속된 수의 합
# 안전지대
# 겹치는 선분의 길이
# 주사위 게임 3


# 평행
# 배열 조각하기
# 정수를 나선형으로 배치하기
# 옹알이 (1)