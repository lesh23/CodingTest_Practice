# 5월 11일
# 약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer +=i
    return answer

# 짝수와 홀수
def solution(num):
    answer = ''
    if num%2==0:
        answer='Even'
    else:
        answer= 'Odd'
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    for i in str(n):
        answer+=int(i)
    return answer

# 5월 12일 
# 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==1:
            return i

# 평균 구하기
def solution(arr):
    answer = 0
    for i in arr:
        answer += float(i)
    return answer/len(arr)

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range (1,n+1):
        answer.append (x*i)
    return answer


# 5월 15일
# 문자열 내 p와 y의 개수
def solution(s):
    cnt_p = 0
    cnt_y = 0 
    for i in s:
        if i=='p' or i=='P':
            cnt_p += 1
        if i=='y' or i=='Y':
            cnt_y += 1
    if cnt_p == cnt_y:
        return True
    else:
        return False

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    l = list(map(int, str(n)))
    answer = l[::-1]
    return answer

# 정수 제곱근 판별
def solution(n):
    answer = 0 
    a = n**0.5
    if a == int(a):
        answer = (a+1)**2
    else : 
        answer = -1
    return answer 

# 5월 17일
# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)

# 정수 내림차순으로 배치하기
def solution(n):
    l = list(str(n))
    for i in range(0,len(l)):
        l[i] = str(l[i])
    l.sort(reverse=True)
    return "".join(map(str, l))

# 하샤드 수
def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x%sum == 0:
        return True
    else:
        return False
    
# 5월 18일
# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a<b: 
        for i in range(a,b+1):
            answer += i
    elif b<a:
        for i in range(b,a+1):
            answer +=i
    elif a==b:
        answer = a
    return answer

# 콜라츠 추측
def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer == 500:
            return -1
    return answer

# 서울에서 김서방 찾기
def solution(seoul):   
    for i in range(0,len(seoul)) :
        if seoul[i] == 'Kim':
            return '김서방은 ' + str(i) + '에 있다'
# 5월 19일
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
# 5월 22일
# 없는 숫자 더하기
def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]    
    return sum(set(arr)-set(numbers))

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
    if len(arr) ==1:
        arr=[-1]
    return arr

# 가운데 글자 가져오기
def solution(s):
    answer = ''
    a=len(s)
    if a%2==1:
        answer = s[a//2]
    else:
        answer = s[a//2-1] +s[a//2]
    return answer


# 5월 24일
# 수박수박수박수박수박수?
# 내적
# 문자열 내림차순으로 배치하기

# 5월 25일 
# 약수의 개수와 덧셈
# 부족한 금액 계산하기
# 문자열 다루기 기본