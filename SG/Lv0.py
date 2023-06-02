### 5월 11일 ###
# 두 수의 곱
def solution(num1, num2):
    answer = num1*num2
    return answer

# 몫 구하기 
def solution(num1, num2):
    answer = num1//num2
    return answer

# 두 수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer

# 나이 출력
def solution(age):
    answer = 2022 - age +1
    return answer





### 5월 12일 ###
# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

# 각도기
def solution(angle):
    answer = 0
    if 0<angle<90:
        answer = 1
    if angle == 90:
        answer =2
    if 90<angle<180:
        answer=3
    if angle == 180:
        answer=4
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2==0:
            answer +=i    
    return answer

# 배열의 평균 값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer+=i       
    return answer/len(numbers)





### 5월 15일 ###
# 양꼬치
def solution(n, k):
    answer = (n*12000)+(k*2000)-(n//10)*2000
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    else :
        answer = 0
    return answer

# 정수 부분
def solution(flo):
    answer = 0                  
    import math
    answer = math.floor(flo)
    return answer

# 대문자로 바꾸기
def solution(myString):
    answer = ''
    answer = myString.upper()
    return answer

# 문자열로 변환
def solution(n):
    answer = ''
    answer = str(n)
    return answer





### 5월 17일 ###
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
    print myString.lower()

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
    




### 5월 18일 ###
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a+b
    else:
        return a-b

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    return 0

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in arr:
            answer.append(i*k)
    else :
        for i in arr:
            answer.append(i+k)
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

# 문자열 곱하기
def solution(my_string, k):
    return (my_string)*k





### 5월 19일 ###
# 문자열의 뒤의 n글자
def solution(my_string, n):
    l=list(my_string)
    result=''.join(map(str,l[len(l)-n:len(l)]))
    return result

# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]   
    return answer

# 점의 위치 구하기
def solution(dot):
    answer = 0
    if dot[0]>0 and dot[1]>0:
        answer = 1
    if dot[0]<0 and dot[1]>0:
        answer = 2
    if dot[0]<0 and dot[1]<0:
        answer = 3
    if dot[0]>0 and dot[1]<0:
        answer = 4
    return answer

# 편지
def solution(message):
    answer = 0
    a=list(message)
    answer = len(a)*2
    return answer





### 5월 22일 ###
# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = 0
    if n%slice ==0:
        answer = n//slice
    else:
        answer = n//slice +1
    return answer

# 피자 나눠 먹기 (1)
def solution(n):
    answer = 0
    if n%7==0:
        answer = n//7
    else : 
        answer = n//7+1
    return answer

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer >n:
            break
    return answer





### 5월 24일 ###
# 중앙값 구하기
def solution(array):
    answer = 0
    array.sort()
    return array[len(array)//2]

# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer += 1
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i> height:
            answer += 1 
    return answer

# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

# 최댓값 만들기(1)
def solution(numbers):
    answer = 0
    new = []
    for i in range(1,len(numbers)):
        new.append(numbers[i-1]*numbers[i])   
    return max(new)

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]  # 리스트로 바꿀 필요 없음

# 삼각형의 완성조건 (1)
def solution(sides):
    answer = 0
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        answer = 1
    else:
        answer = 2       
    return answer

# 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

# 짝수 홀수 개수
def solution(num_list):
    answer = []
    a=0 
    b=0
    for i in num_list:
        if i%2==0:
            a+=1
        else:
            b+=1
    answer = [a,b]        
    return answer

# 길이에 따른 연산
def solution(num_list):
    answer = 1
    if len(num_list) > 10 :
        answer = sum(num_list)
    else : 
        for i in num_list:
            answer *= i
    return answer





### 5/25 ###
# 옷가게 할인 받기
def solution(price):
    answer = 0
    if price < 100000 : 
        answer = int(price)
    if 300000 > price >= 100000 : 
        answer = int(price * 0.95)
    if 500000 > price >= 300000 :
        answer = int(price * 0.9)
    if price >= 500000:
        answer = int(price * 0.8)
    return answer

# 아이스 아메리카노
def solution(money):
    return [money//5500, money%5500]

# 첫 번째로 나오는 음수
def solution(num_list):
    for i in range(0,len(num_list)):
        if num_list[i]<0:
            return i
    return -1

# 모음 제거
def solution(my_string):
    for i in ["a","e","i","o","u"]:
        if i in my_string:
            my_string=my_string.replace(i,"")
    return my_string    

# 원소들의 곱과 합
def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    if a < b**2:
        return 1
    else:
        return 0

# 정수 찾기
def solution(num_list, n):
    if n in num_list:
        return 1
    return 0

# 주사위 게임 1
def solution(a, b):
    answer = 0
    if a%2==1 and b%2==1:
        answer = (a**2)+(b**2)
    elif a%2==1 or b%2==1:
        answer = 2*(a+b)
    elif a%2==0 and b%2==0:
        answer = abs(a-b)
    return answer

# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# 뒤에서 5등 위로
def solution(num_list):
    answer = []
    l = sorted(num_list)
    return l[5:]

# 공백으로 구분하기 1
def solution(my_string):
    return my_string.split()





### 5월 26일 ### 
# rny_string
def solution(rny_string):
    return rny_string.replace("m","rn")

# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i==j:
                answer +=1
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

# 자릿수 더하기 ver.1
def solution(n):
    answer = 0
    for i in str(n):
        answer+= int(i)
    return answer

# 자릿수 더하기 ver.2 - while문 사용
def solution(n):
    answer = 0
    while n:
        answer += n%10
        n = n//10
    return answer
        
# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2 == 1:
            answer.append(i)
    return answer

# 카운트 업
def solution(start, end):
    answer = []
    for i in range(start,end+1):
        answer.append(i)
    return answer

# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    return 0

# 카운트 다운
def solution(start, end):
    answer = []
    for i in range(end,start+1):
        answer.append(i)
    return answer[::-1]

# n개 간격의 원소들
def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list)):
        if i%n==0:
            answer.append(num_list[i])
    return answer





### 5월 29일 ###
# 문자열 정수의 합
def solution(num_str):
    answer = 0
    for i in str(num_str):
        answer += int(i)
    return answer

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            answer+=int(i)
    return answer

#문자열 붙여서 출력하기
a = input()
print(a.replace(" ",""))

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = []
    l = list(my_string)
    for i in index_list:
        answer.append(l[i])
    return ''.join(answer)

# 원하는 문자열 찾기
def solution(myString, pat):
    if pat.upper() in myString.upper() :
        return 1
    return 0

# 배열 만들기 1
def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if i%k==0:
            answer.append(i)
    return answer

# 홀짝 구분하기
a = int(input())
if a%2 == 0:
    print("%a is even" %a)
else :
    print("%a is odd" %a)

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer = []
    for i in arr:
        if i>=50 and i%2==0:
            answer.append(i/2)
        elif i<50 and i%2==1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer

# 수 조작하기 1
def solution(n, control):
    answer = n
    for i in control:
        if i == "w":
            answer += 1
        elif i == "s":
            answer -= 1
        elif i == "d":
            answer += 10
        elif i == "a":
            answer -= 10
    return answer

# 뒤에서 5등까지
def solution(num_list):    
    return sorted(num_list)[0:5]





### 5월 31일 ###
# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    answer = []
    for i in range(0,len(strArr)):
        if i%2==0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())       
    return answer

# 문자열안에 문자열
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

# 제곱수 판별하기
def solution(n):
    answer = 0
    for i in range(0,n-1):
        if (n **(0.5)).is_integer():
            answer = 1
        else:
            answer = 2
    return answer

# 이어 붙인 수
def solution(num_list):
    l = list(map(str,num_list))
    a = ''
    b = ''
    for i in l:
        if int(i)%2==1:
            a += i
        else:
            b += i
    return int(a)+int(b)

# 문자열 바꿔서 찾기 (어려움,,ㅠㅜ)
def solution(myString, pat):
    answer = []
    l = list(myString)
    for i in l:
        if i == "A":
            answer.append("B")
        else:
            answer.append("A")
    result = ''.join(map(str, answer))
    if pat in result:
        return 1
    return 0

# 개미 군단
def solution(hp):
    answer = hp // 5
    hp = hp % 5
    answer += hp // 3
    hp = hp % 3
    answer += hp
    return answer

# 문자열 바꿔서 찾기(중복)

# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = []
    for i in range(1,len(my_string)-1):
        answer.append(my_string[:i])
    if is_prefix in answer:
        return 1
    return 0

# 더 크게 합치기
def solution(a, b):
    answer = [str(a)+str(b),str(b)+str(a)]
    return int(max(answer))

# 마지막 두 원소
def solution(num_list):
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(2*(num_list[-1]))
    return num_list





### 6월 1일 ###
# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

# 암호 해독
def solution(cipher, code):
    answer = ''
    l = list(cipher)
    for i in range(0,len(l)):
        if (i+1)%code==0:
            answer += l[i]
    return answer

# 가위 바위 보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        if i=="0":
            answer += "5"
        if i=="5":
            answer += "2"
    return answer

# 세균 증식
def solution(n, t):
    return n*(2**t)

# 홀짝에 따라 다른 값 반환하기
def solution(n):
    answer = 0
    if n%2==1:
        for i in range(0,int(n/2)+1):
            answer += 2*i+1
    if n%2==0:
        for j in range(0,int(n/2)+1):
            answer += (j*2)**2            
    return answer

# 대문자와 소문자
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper() == True:
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

# 주사위의 개수
def solution(box, n):
    answer = 1
    for i in box:
        answer *= int(i/n)
    return answer

# 공백으로 구분하기 2
def solution(my_string):
    answer = []
    l = my_string.split(' ')
    for i in l:
        if i != "":
            answer.append(i)
    return answer

# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(a,"+",b,"=",a+b)

# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for j in arr:
        answer += [j]*j
    return answer





### 6월 2일 ###
# 부분 문자열 이어 붙여 문자열 만들기
# 직각삼각형 출력하기
n = int(input())
for i in range(1,n+1):
    print ("*"*i, end = "\n")

# 문자열 정렬하기 (1)
def solution(my_string):
    answer = []
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in my_string:
        if i.isalpha() == False:
            answer.append(int(i))
    answer.sort()
    return answer

# 최댓값 만들기 (2)
# 홀수 vs 짝수

# n의 배수 고르기
# 배열의 길이에 따라 다른 연산하기
# 접미사인지 확인하기
# A 강조하기
# 배열 회전시키기
