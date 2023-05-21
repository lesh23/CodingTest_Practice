# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor ==0:
            answer.append(i)
    if len(answer) ==0:
        answer.append(-1)
    else:
        answer.sort()
    return answer

# 핸드폰 번호 가리기
def solution(phone_number):
    star = "*"*(len(phone_number)-4)
    return star + phone_number[-4:]
    
# 음양 더하기
def solution(absolutes, signs):
    answer = []
    for i in range(len(signs)):
        if signs[i] is True:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    return sum(answer)