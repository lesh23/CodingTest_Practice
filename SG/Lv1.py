### 5월 11일 ###
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



### 5월 12일 ###
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



### 5월 15일 ###
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



### 5월 17일 ###
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



### 5월 18일 ###
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



### 5월 19일 ###
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



### 5월 22일 ###
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



### 5월 24일 ###
# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    if n%2==0:
        answer = "수박"*(n/2)
    else:
        answer = "수박"*(n/2)+"수"
    return answer

# 내적
def solution(a, b):
    answer = []
    n = 0
    while n!= len(a) :
        answer.append(a[n]*b[n])
        n += 1
    return sum(answer)

# 문자열 내림차순으로 배치하기
def solution(s):
    return ''.join(sorted(s, reverse = True))



### 5월 25일 ###
# 약수의 개수와 덧셈
def solution(left, right):
    def gcm(i):        
        b = 0
        for j in range(1, i+1):
            if i % j == 0:
                b+=1
        return b
    answer = 0
    l = list(range(left,right+1))
    for i in l:
        if gcm(i)%2==0:
            answer += i
        else:
            answer -= i
    return answer

# 부족한 금액 계산하기
def solution(price, money, count):
    s = 0
    for i in range(1,count+1):
        s += price*i
    if s>money:
        return s-money
    if s<=money:
        return 0
    
# 문자열 다루기 기본
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        return True
    else:
        return False



### 5월 26일 ###
# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    for i in range(0,len(arr1)):
        s = []
        for j in range(0,len(arr1[0])):
            s.append(arr1[i][j] + arr2[i][j])
        answer.append(s)        
    return answer

# 직사각형 별찍기
a, b = map(int, raw_input().strip().split(' '))
for i in range(b):
    print('*'*a)

# 최대공약수와 최소공배수
def solution(n, m):
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            a = i
            b = (n*m)/i
    return [a,b]



### 5월 29일 ###
# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 3진법 뒤집기
def solution(n):
    answer = 0
    l=[]
    while n:
        l.append(n%3)
        n = n//3
    for i in range(len(l)):
        answer*=3
        answer+=l[i]
    return answer

# 이상한 문자 만들기
def solution(s):
    answer = ''
    l = s.split(' ')
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if j%2==0:
                s1 = l[i][j]            # 이 과정 생략하고 l[i][j].upper() 하면 왜 자꾸 오류가 나는 것일까 !!
                s2 = s1.upper()
                answer += s2
            else:
                s3 = l[i][j]
                s4 = s3.lower()
                answer += s4
        answer += ' '
    return answer[0:-1]



### 5월 30일 ###
# 예산
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i 
        if budget < 0:
            break   
        answer += 1                 
    return answer

# 시저 암호
def solution(s, n):
    answer = ''
    import string
    l_s = list(string.ascii_lowercase)+list(string.ascii_lowercase)
    u_s = list(string.ascii_uppercase)+list(string.ascii_uppercase)
    for i in s:
        for j in range(0,int(len(l_s)/2)):
            if i in l_s[j]:
                answer += l_s[j+n]
            if i in u_s[j]:
                answer += u_s[j+n]
        if i == ' ':
            answer += ' '
    return answer

# 삼총사 ver.1 for문 사용
def solution(number):
    answer = 0
    for i in range(0,len(number)-2):            # 범위 주의
        for j in range(i+1,len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

# 삼총사 ver.2 라이브러리 이용
def solution(number):
    answer = 0
    from itertools import combinations
    l = list(combinations(number, 3))
    for i in l:
        if sum(i)==0:
            answer += 1
    return answer



# 5월 31일
# 최소직사각형
def solution(sizes):
    answer = 0
    long = []
    short = []
    for i in sizes:
        long.append(max(i))
        short.append(min(i))
    return max(long)*max(short)

# [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    a = ''
    for i in range(0,n):
        answer.append(bin(arr1[i]|arr2[i])[2:])
    for k in range(0,n):
        if len(answer[k])<n:
            answer[k] = '0'*(n-len(answer[k]))+answer[k]
            print(answer)
    for j in range(0,n):
        answer[j] = answer[j].replace('1','#')
        answer[j] = answer[j].replace('0',' ')
    return answer
    
# 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0 
    n = len(p)
    for i in range(0,len(t)-n+1):
        if t[i:i+len(p)] <= p:
            answer += 1
    return answer



### 6월 1일 ###
# 숫자 문자열과 영단어	
# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    new = []
    for i in range(0,len(strings)):
        strings[i] = strings[i][n]+strings[i]
    for i in range(0,len(strings)):
        answer.append(sorted(strings)[i][1:])
    return answer

# K번째수
def solution(array, commands):
    answer = []
    new = []
    for i in range(0,len(commands)):
        new = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(new[(commands[i][2])-1])
    return answer

