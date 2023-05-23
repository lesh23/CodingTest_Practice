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
    answer = lambda i,j,k: 1 if i%n==0 and i%m==0 else 0
    return answer(number, n, m)