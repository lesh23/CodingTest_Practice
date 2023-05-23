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