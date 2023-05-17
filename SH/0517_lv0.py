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