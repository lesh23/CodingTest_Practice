# 숫자 비교하기
def solution(num1, num2):
    answer = 0
    if num1 != num2:
        answer = -1
    else :
        answer = 1
    return answer

# 소문자로 바꾸기
def solution(myString):
    return myString.lower()

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''
    for i in arr:
        answer += str(i)
    return answer

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 공배수
def solution(number, n, m):
    if number%n == 0 and number%m==0 :
        return 1
    else:
        return 0