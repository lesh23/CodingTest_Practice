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
    