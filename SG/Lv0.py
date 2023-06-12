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





### 5월 30일 ###
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





### 5월 31일 ###
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

# 대문자와 소문자 ver.2
def solution(my_string):
    return my_string.swapcase()

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

# 공백으로 구분하기 2 ver.2
def solution(my_string):
    return my_String.split() # 공백을 무시하는 것

# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(a,"+",b,"=",a+b)

# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for j in arr:
        answer += [j]*j
    return answer





### 6월 1일 ###
# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(0,len(my_strings)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer

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
def solution(numbers):
    new = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):            
            new.append(numbers[i]*numbers[j])
    return max(new)

# 홀수 vs 짝수
def solution(num_list):
    odd = 0
    even = 0
    for i in range(0,len(num_list)):
        if i%2==0:
            odd += num_list[i]
        else:
            even += num_list[i]
    return max(odd,even)

# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
    return answer

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    answer = []
    if len(arr)%2==1:
        for i in range(0,int((len(arr)-1)/2)+1):
            arr[2*i] += n
    if len(arr)%2==0:
        for i in range(0,int(len(arr)/2)):
            arr[2*i+1] += n
    return arr

# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = []
    for i in range(0,len(my_string)):
        answer.append(my_string[i:])
    if is_suffix in answer:
        return 1
    else:
        return 0
    
# A 강조하기
def solution(myString):
    answer = ''
    for i in range(0,len(myString)):
        if myString[i] == 'a' or myString[i] == 'A':
            answer += 'A'
        else:
            answer += myString[i].lower()
    return answer

# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    two = numbers+numbers
    if direction == "right":
        answer = [numbers[-1]]+numbers[0:len(numbers)-1]
    if direction == "left":
        answer = numbers[1:len(numbers)]+[numbers[0]]
    return answer





### 6월 2일 ###
# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1],answer[num2] = answer[num2],answer[num1]
    return ''.join(answer)

# 외계행성의 나이
def solution(age):
    answer = []
    for i in str(age):
        answer.append(int(i))
    for j in range(0,len(answer)):
        answer[j] = chr(answer[j]+97)
    return ''.join(answer)

# 가장 큰 수 찾기
def solution(array):
    return [max(array),array.index(max(array))]

# 접미사 배열
def solution(my_string):
    answer = []
    for i in range(0,len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer)

# 피자 나눠 먹기 (2)
def solution(n):
    import math
    return n/math.gcd(n,6)

# 0 떼기
def solution(n_str):
    return str(int(n_str))

# 문자열 섞기
# 369게임
def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i=='6' or i=='9':
            answer +=1
    return answer

# 5명씩
def solution(names):
    answer = []
    for i in range(0,len(names)):
        if i%5==0:
            answer.append(names[i])
    return answer

#l로 만들기
def solution(myString):
    answer = list(myString)
    for i in range(0,len(answer)):
        if ord(answer[i]) < ord('l'):
            answer[i] = 'l'
    return ''.join(answer)





### 6월 7일 ###
# 약수 구하기
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i==0:
            answer.append(i)
    return answer

# 문자열 돌리기
str = input()
for i in str:
    print(i)

# 배열 비교하기
def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1    
    return answer

# 숫자 찾기
def solution(num, k):
    answer = 0
    l = list(str(num))
    for m,n in enumerate(l):
        if n == str(k):
            return m+1
    return -1

# ad 제거하기
def solution(strArr):
    answer = []
    for i in range(0,len(strArr)):
        if "ad" not in strArr[i]:
            answer.append(strArr[i])
    return answer

# 할 일 목록
def solution(todo_list, finished):
    answer = []
    for i in range(0,len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer

# 간단한 식 계산하기
def solution(binomial):
    [num1,c,num2] = binomial.split()
    if c == '+':
        return int(num1)+int(num2)
    elif c== '-':
        return int(num1)-int(num2)
    elif c== '*':
        return int(num1)*int(num2)
    
# 콜라츠 수열 만들기
def solution(n):
    answer = [n]
    while n != 1:
        if n%2==0:
            n = n/2
            answer.append(n)
        else:
            n = 3*n+1
            answer.append(n)
    return answer

# 배열의 원소 삭제하기
def solution(arr, delete_list):
    answer = []
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer

# 문자열 정렬하기 (2)
def solution(my_string):
    answer = ''
    l = list(my_string.lower())
    l.sort()
    return ''.join(l)





### 6월 8일 ###
# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if len([j for j in range(1, i+1) if i%j==0]) != 2:
            answer += 1
    return answer

# 가까운 1 찾기
def solution(arr, idx):
    answer = []
    for i in range(0,len(arr)):
        if arr[i] ==1 and i>= idx:
            return i
    else:
        return -1
    
# 주사위 게임 2
def solution(a, b, c):
    answer = 0
    if a==b==c:
        answer = (a+b+c)*((a**2)+(b**2)+(c**2))*((a**3)+(b**3)+(c**3))
    elif a==b or a==c or b==c:
        answer = (a+b+c)*((a**2)+(b**2)+(c**2))
    else:
        answer = a+b+c
    return answer

# 특별한 이차원 배열 2
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# 순서 바꾸기
def solution(num_list, n):
    answer = []
    return num_list[n:]+num_list[:n]


# 9로 나눈 나머지
def solution(number):
    return sum(list(map(int,number)))%9

# 중복된 문자 제거
def solution(my_string):
    answer = []
    l = list(map(str,my_string))
    for i in l:
        if i not in answer:
            answer.append(i)
    return ''.join(answer)

# 모스부호 (1)
def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    for i in letter.split():
        answer += morse[i]
    return answer

# x 사이의 개수
def solution(myString):
    answer = []
    s = myString.split("x")
    for i in s:
        answer.append(len(i))
    return answer

# 배열 만들기 3
def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]





### 6월 9일 ###
# 팩토리얼
def solution(n):
    answer = 1
    for i in range(2,11):
        answer *= i
        if answer > n:
            return i-1
        elif answer == n:
            return i

# A로 B 만들기
def solution(before, after):
    answer = 0
    if sorted(list(before)) == sorted(list(after)) :
        return 1
    return 0

# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    for i in range(int(len(num_list)/n)):
        answer.append(num_list[n*i:n*i+n])
    return answer

# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + i*d
    return answer

# 가까운 수
def solution(array, n):
    answer = []
    lis = []
    for i in array:
        lis.append(abs(i-n))
    for j in range(len(lis)):
        if lis[j] == min(lis):
            answer.append(array[j])
    return min(answer)

# 두 수의 연산값 비교하기
def solution(a, b):
    return max(int(str(a)+str(b)),2*a*b)

# k의 개수
def solution(i, j, k):
    s = ''
    for i in range(i,j+1):
        s += str(i)
    lis = list(s)
    return lis.count(str(k))

# 진료순서 정하기
def solution(emergency):
    answer = []
    lis = sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(lis.index(i)+1)        
    return answer

# 문자열 잘라서 정렬하기
def solution(myString):
    return sorted(' '.join(myString.split('x')).split())

# 문자열 반복해서 출력하기
a, b = input().strip().split(' ')
b = int(b)
print(a*b)






### 6월 12일 ###
# 특별한 이차원 배열 1
def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)] 
    for i in range(len(answer)):
            answer[i][i] = 1
    return answer

# 숨어있는 숫자의 덧셈 (2)

# 한 번만 등장한 문자
def solution(s):
    answer = ''
    for i in s:
        if s.count(i) ==1:
            answer += i
    return ''.join(sorted(answer))

# 수 조작하기 2
def solution(numLog):
    answer = ''
    result = []
    for i in range(len(numLog)-1):
        result.append(numLog[i+1]-numLog[i])
    for j in result:
        if j==1:
            answer +='w'
        elif j==-1:
            answer +='s'
        elif j== 10:
            answer +='d'
        elif j== -10:
            answer +='a'
    return answer

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    return (x1|x2)&(x3|x4)

# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    ret = []
    for i in intStrs:
        ret.append(i[s:s+l])
    for j in ret:
        if int(j)>k:
            answer.append(int(j))
    return answer

# 수열과 구간 쿼리 3
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr


# 문자열 뒤집기
def solution(my_string, s, e):
    lis = list(my_string)[:s] + list(my_string)[s:e+1][::-1] + list(my_string)[e+1:]
    return ''.join(lis)

# 이진수 더하기
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]

# 1로 만들기
def solution(num_list):
    answer = 0
    for i in num_list:
        cnt = 0
        while i != 1:
            if i%2==0:
                i = i/2
            else:
                i = (i-1)/2
            cnt += 1
        answer += cnt
    return answer





### 6월 13일 ###
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





### 6월 14일 ###
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





### 6월 15일 ###
# 삼각형의 완성조건 (2)
# 수열과 구간 쿼리 4
# 리스트 자르기
# 외계어 사전
# qr code

# a와 b 출력하기
# 조건 문자열
#2의 영역
# 배열의 길이를 2의 거듭제곱으로 만들기
#커피 심부름





### 6월 16일 ###
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





### 6월 19일 ###
# 등수 매기기
# 유한소수 판별하기
# 대소문자 바꿔서 출력하기
# 저주의 숫자 3
# 특이한 정렬

#문자열 여러 번 뒤집기
# 문자열 밀기
# 정사각형으로 만들기
# 왼쪽 오른쪽
# 그림 확대





### 6월 20일 ###
# 무작위로 K개의 수 뽑기
# 다항식 더하기
# 배열 만들기 6
#전국 대회 선발 고사
# 최빈값 구하기

# 배열 만들기 2
#문자열 출력하기
#OX퀴즈
# 코드 처리하기
#분수의 덧셈





### 6월 21일 ###
# 다음에 올 숫자
# 연속된 수의 합
# 안전지대
# 겹치는 선분의 길이
# 주사위 게임 3

# 평행
# 배열 조각하기
# 정수를 나선형으로 배치하기
# 옹알이 (1)