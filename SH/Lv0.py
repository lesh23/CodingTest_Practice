### 5/11
# 두 수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 몫 구하기 
def solution(num1, num2):
    return num1 // num2

# 두 수의 차
def solution(num1, num2):
    return num1-num2

# 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 나이 출력
def solution(age):
    answer = 2022-age+1
    return answer



### 5/12
# 두 수의 합
solution = lambda num1, num2 : num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return (num1*1000) // num2

# 각도기
def solution(angle):
    if angle < 90 :
        answer = 1
    elif angle == 90 :
        answer =2
    elif angle >90 and angle <180:
        answer=3
    else :
        answer=4
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0 :
            answer += i        
    return answer

# 배열의 평균 값
# 라이브러리 사용
import numpy as np
def solution(numbers):
    answer = np.mean(numbers)
    return answer

# 라이브러리 사용 X
def solution(numbers):
    return sum(numbers) / len(numbers)



###5/15
# 양꼬치
def solution(n, k):
    a = k-(n //10)
    if a <= 0 :
        answer = n*12000
    else :
        answer = n*12000 + a*2000
    return answer

# n의 배수
def solution(num, n):
    answer = 0
    if num % n ==0:
        answer =1
    return answer

# 정수 부분
def solution(flo):
    answer = int(flo)
    return answer

# 대문자로 바꾸기
def solution(myString):
    answer = myString.upper()
    return answer

# 문자열로 변환
def solution(n):
    return str(n)



### 5/17
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



### 5/18
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag == True:
        return a+b
    else :
        return a-b
    
# 부분 문자열
def solution(str1, str2):
    answer = lambda x,y : 1 if y.count(x) !=0 else 0
    return answer(str1, str2)

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 ==1:
        for i in arr:
            answer.append(i*k)
    else :
        for i in arr:
            answer.append(i+k)
    
    return answer

# 배열 두 배 만들기
def solution(numbers):
    return [i*2 for i in numbers]

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k



### 5/19
# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 배열 뒤집기
def solution(num_list):
    return list(reversed(num_list))

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1]>0:
        return 1
    elif dot[0] < 0 and dot[1]>0:
        return 2
    elif dot[0] < 0 and dot[1]<0:
        return 3
    else:
        return 4

# 편지
def solution(message):
    return len(message)*2



### 5/22
# 배열 원소의 길이
def solution(strlist):
    answer = []
    
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    if letter in my_string:
        return my_string.replace(letter,'')
    else:
        return my_string

def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    
    return answer

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = lambda x, y : y // x if y % x == 0 else y//x +1
    return answer(slice, n)

# 피자 나눠 먹기 (1)
def solution(n):

    if n % 7 == 0:
        return n // 7
    
    return n // 7 +1

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        
        if answer > n:
            break
    return answer



### 5/24
# 중앙값 구하기
def solution(array):
    array.sort()
    return array[int(len(array)/2)]

# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i ==0:
            answer += 1
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    return sum(1 if x > height else 0 for x in array)

# 중복된 숫자 개수
def solution(array, n):
    return array.count(n)

# 최댓값 만들기(1)
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# 삼각형의 완성조건 (1)
def solution(sides):
    a = sides.pop(sides.index(max(sides)))
    if a < sum(sides):
        return 1
    return 2

# 문자열 뒤집기
def solution(my_string):
    my_string = list(my_string)
    return ''.join(my_string[::-1])

# 짝수 홀수 개수
def solution(num_list):
    answer = [0,0]
    
    for i in num_list:
        if i%2 == 0:
            answer[0] += 1
        else :   
            answer[1] += 1
    
    return answer

# 길이에 따른 연산
def solution(num_list):
    if len(num_list) >=11:
        return sum(num_list)
    else :
        answer = 1
        for i in num_list:
            answer *= i
    
    return answer



### 5/25
# 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    else :
        return int(price)
    
# 아이스 아메리카노
def solution(money):
    return [money//5500, money%5500]

# 첫 번째로 나오는 음수
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] <0:
            return i
    return -1

# 모음 제거
def solution(my_string):
    for i in ['a','e','i','o','u']:
        my_string = my_string.replace(i,'')
    return my_string

# 원소들의 곱과 합
def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    if mul < sum(num_list) ** 2 :
        return 1
    return 0

# 정수 찾기
def solution(num_list, n):
    if n in num_list:
        return 1
    return 0

# 주사위 게임 1
def solution(a, b):
    if a*b % 2 ==1:
        return a**2 + b**2
    elif (a+b) % 2 ==1:
        return 2*(a+b)
    else:
        return abs(a-b)
    
# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# 뒤에서 5등 위로
def solution(num_list):
    num_list.sort()
    return num_list[5:]

# 공백으로 구분하기 1
def solution(my_string):
    return my_string.split(' ')



### 5/26
# rny_string
def solution(rny_string):
    return rny_string.replace('m','rn')

# 배열의 유사도
def solution(s1, s2):
    return sum(1 if i in s2 else 0 for i in s1)

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

# 자릿수 더하기
def solution(n):
    return sum(int(x) for x in str(n))

# n 번째 원소부터
def solution(num_list, n):
     return num_list[n-1:]

# 짝수는 싫어요
def solution(n):
    return [x for x in range(n+1) if x%2==1]

# 카운트 업
def solution(start, end):        
    return [x for x in range(start,end+1)]

# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    return 0

# 카운트 다운
def solution(start, end):
    return [x for x in range(start,end-1,-1)]

# n개 간격의 원소들
def solution(num_list, n):
    return num_list[::n]



### 5/29
# 문자열 정수의 합
def solution(num_str):
    return sum(list(map(int, num_str)))

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    l = [str(x) for x in range(10)]
    answer = 0 
    for i in my_string:
        if i in l:
            answer += int(i)
    return answer

# 풀이2 (isdigit 사용)
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

# 풀이3 (정규표현식 사용)
import re
def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1+str2)

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])

# 원하는 문자열 찾기
def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    return 0

# 배열 만들기 1
def solution(n, k):
    return [x for x in range(1,n+1) if x%k==0]

# 홀짝 구분하기
a = int(input())
if a%2 == 0:
    print(str(a) + ' is even')
else:
    print(str(a) + ' is odd')

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i]%2 == 0:
            arr[i] //= 2
        elif arr[i]<50 and arr[i]%2 ==1:
            arr[i] *= 2
    return arr

# 수 조작하기 1
def solution(n, control):
    n += control.count('w')
    n -= control.count('s')
    n += control.count('d')*10
    n -= control.count('a')*10
    return n

# 뒤에서 5등까지
def solution(num_list):
    return sorted(num_list)[:5]



### 5/30
# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for i in range(len(strArr)):
        if i%2==0:
            strArr[i] = strArr[i].lower()
        else :
            strArr[i] = strArr[i].upper()
    return strArr

# 문자열안에 문자열
def solution(str1, str2):
    answer = lambda x,y : 1 if str2 in str1 else 2
    return answer(str1,str2)

# 제곱수 판별하기
from math import sqrt
def solution(n):
    if n % int(sqrt(n)) == 0:
        return 1
    else: 
        return 2

    # 다른 풀이
    def solution(n):
        return 1 if (n ** 0.5).is_integer() else 2

# 이어 붙인 수
def solution(num_list):
    e =''
    o = ''
    for i in num_list:
        if i % 2 ==0:
            e += str(i)
        else :
            o += str(i)
    return int(e)+int(o)

# 문자열 바꿔서 찾기
def solution(myString, pat):
    myString = myString.replace('A','C')
    myString = myString.replace('B','D')
    
    pat = pat.replace('A','D')
    pat = pat.replace('B','C')

    if pat in myString:
        return 1
    else:
        return 0
    
# 개미 군단
def solution(hp):
    result = 0
    while hp >0:
        if hp // 5 >= 1:
            result += hp//5
            hp =  hp% 5
        elif hp // 3 >= 1:
            result += hp //3
            hp = hp % 3
        else :
            result += hp
            hp = 0
    return result

# 문자열 바꿔서 찾기
def solution(myString, pat):
    myString = myString.replace('A','C')
    myString = myString.replace('B','D')
    
    pat = pat.replace('A','D')
    pat = pat.replace('B','C')

    if pat in myString:
        return 1
    else:
        return 0
    
# 접두사인지 확인하기
def solution(my_string, is_prefix):
    if is_prefix not in my_string:
        return 0
    
    if my_string[:len(is_prefix)] == is_prefix :
        return 1
        
    return 0

# 내장함수 이용
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

# 더 크게 합치기
def solution(a, b):
    return max(int(str(a)+str(b)),int(str(b)+str(a)))

# 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(2*num_list[-1])
    return num_list



### 5/31
# 꼬리 문자열
def solution(str_list, ex):
    answer = []
    for i in str_list:
        if ex not in i :
            answer.append(i)
    return ''.join(answer)

# 암호 해독
def solution(cipher, code):
    answer = [cipher[i] for i in range(code-1, len(cipher),code)]
    return ''.join(answer)

# 가위 바위 보
def solution(rsp):
    rsp = list(rsp)
    for i in range(len(rsp)) :
        if rsp[i] =='2' :
            rsp[i] = '0'
        elif rsp[i] =='0':
            rsp[i] = '5'
        else : 
            rsp[i]='2'
    return ''.join(rsp)

    # dic 쓰는거 확인
    def solution(rsp):
        d = {'0':'5','2':'0','5':'2'}
        return ''.join(d[i] for i in rsp)

# 세균 증식
def solution(n, t):
    return n * (2**t)

# 홀짝에 따라 다른 값 반환하기
def solution(n):
    if n % 2 ==1 :
        return sum([x for x in range(1,n+1,2)])
    else:
        return sum([x**2 for x in range(0,n+1,2)])
    
# 대문자와 소문자
def solution(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i].isupper() == True:
            my_string[i] = my_string[i].lower()
        else :
            my_string[i] = my_string[i].upper()
    return ''.join(my_string)

    # 내장함수
    def solution(my_string):
        return my_string.swapcase()

# 주사위의 개수
def solution(box, n):
    answer = 1
    for i in box:
        answer *= i//n
    return answer

    # 따로따로 변수 선언
    def solution(box, n):
        x, y, z = box
        return (x // n) * (y // n) * (z // n )

# 공백으로 구분하기 2
def solution(my_string):
    my_string = my_string.split(' ')

    while '' in my_string:
        my_string.remove('')
    return my_string

    # 그냥 split()으로 해도됨
    # my_string.split() 하면 알아서 공백 다 제거하고 return 

# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(str(a)+ ' + '+str(b) +' = ' +str(a+b))

# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []

    for i in arr :
        j=i
        while j >0:
            answer.append(i)
            j -= 1
    return answer




### 6/1 
# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer

    # enumerate 이용해보기

# 직각삼각형 출력하기
n = int(input())
for i in range(1,n+1):
    print('*'*i)

# 문자열 정렬하기 (1)
def solution(my_string):
    answer = [int(x) for x in my_string if x.isdigit()==True]
    return sorted(answer)

# 최댓값 만들기 (2)
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])

# 홀수 vs 짝수
def solution(num_list):
    return max(sum(x for x in num_list[::2]), sum(x for x in num_list[1::2]))

# n의 배수 고르기
def solution(n, numlist):
    return [x for x in numlist if x % n ==0]

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    if len(arr) % 2 == 0:
        for i in range(1,len(arr),2):
            arr[i] += n
    else :
        for i in range(0,len(arr),2):
            arr[i] += n
    return arr

# 접미사인지 확인하기
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix :
        return 1
    return 0

# A 강조하기
def solution(myString):
    myString = myString.lower()
    myString = myString.replace('a',"A")
    return myString

# 배열 회전시키기
def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]]+numbers[:-1]
    return numbers[1:]+[numbers[0]]



### 6/2
# 인덱스 바꾸기
def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)

# 외계행성의 나이
def solution(age):
    return ''.join([chr(int(x)+97) for x in str(age)])

# 가장 큰 수 찾기
def solution(array):
    return [max(array),array.index(max(array))]

# 접미사 배열
def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])

# 피자 나눠 먹기 (2)
import math
def solution(n):
    return n/math.gcd(n,6)

# 0 떼기
def solution(n_str):
    n_str = list(n_str)
    while True:
        if n_str[0] != '0':
            break
        else:
            n_str.remove('0')
    return ''.join(n_str)

    # answer = str(int(n_str))

# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

# 369게임
def solution(order):
    answer = 0
    for i in str(order):
        if int(i) % 3 ==0 and int(i) != 0:
            answer += 1
    return answer

# 5명씩
def solution(names):
    return [x for x in names[::5]]

# l로 만들기
def solution(myString):
    myString = list(myString)
    for i in range(len(myString)):
        if ord(myString[i]) < ord('l'):
            myString[i] = 'l'
    return ''.join(myString)



### 6/7
# 약수 구하기
def solution(n):
    return [i for i in range(1,n+1) if n % i ==0]

# 문자열 돌리기
str = input()
for i in range(len(str)):
    print(str[i])

# 배열 비교하기
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else :
            return 0
        
# 숫자 찾기
def solution(num, k):
    return str(num).index(str(k))+1 if str(k) in str(num) else -1

# ad 제거하기
def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' not in i:
            answer.append(i)
    return answer

# 할 일 목록
def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(todo_list)) if finished[i] == False]

# 간단한 식 계산하기
def solution(binomial):
    if binomial.split()[1] == '+':
        return int(binomial.split()[0]) + int(binomial.split()[2])
    elif binomial.split()[1] == '-':
        return int(binomial.split()[0]) - int(binomial.split()[2])
    else:
        return int(binomial.split()[0]) * int(binomial.split()[2])
 
    # 내장함수 : eval
    # def solution(binomial):
    #     return eval(binomial)

# 콜라츠 수열 만들기
def solution(n):
    result = [n]
    while n != 1:
        if n %2 ==0:
            result.append(n//2)
            n = n//2
        else :
            result.append(3*n+1)
            n = 3*n+1
    return result

# 배열의 원소 삭제하기
def solution(arr, delete_list):
    for i in delete_list:
        if i in arr :
            arr.remove(i)
    return arr

# 문자열 정렬하기 (2)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))



### 6/8
# 합성수 찾기
def solution(n):
    answer = 0

    if n == 1 or n == 2:
        return answer

    if n>=3 :

        for i in range(3,n+1):

            for j in range(2,i):
                if i % j == 0 :
                    answer +=1
                    break
        
    return answer

# 가까운 1 찾기
def solution(arr, idx):
    for i in range(idx,len(arr)):
        if arr[i] == 1:
            return i
    return -1

# 주사위 게임 2
def solution(a, b, c):
    if len(set([a,b,c])) == 3:
        return a+b+c
    elif len(set([a,b,c])) == 1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        return (a+b+c)*(a**2+b**2+c**2)
    
# 특별한 이차원 배열 2
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# 순서 바꾸기
def solution(num_list, n):
    return num_list[n:] + num_list[:n]

# 9로 나눈 나머지
def solution(number):
    return sum(map(int, str(number))) % 9

# 중복된 문자 제거
def solution(my_string):
    answer = [my_string[0]]
    for i in range(1,len(my_string)):
        if my_string[i] not in answer :
            answer.append(my_string[i])
    return ''.join(answer)

    # 다른사람 풀이
    # def solution(my_string):
    #     answer = ''
    #     for i in my_string:
    #         if i not in answer:
    #             answer+=i
    #     return answer

# 모스부호 (1)
def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    for i in letter.split(' '):
        for j in morse.keys():
            if i==j:
                answer+=morse[j]
    return answer

# x 사이의 개수
def solution(myString):
    answer = []
    for i in myString.split('x'):
        answer.append(len(i))
    return answer

# 배열 만들기 3
def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]



### 6/9
# 팩토리얼
def solution(n):
    a=1
    for i in range(2,12):
        a *= i
        if a > n :
            return i-1
        
# A로 B 만들기
def solution(before, after):
    if sorted(list(before)) == sorted(list(after)) :
        return 1
    return 0

# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n) :
        answer.append(num_list[i:i+n])
    return answer

# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True : 
            answer += a + d*i
    return answer

# 가까운 수
def solution(array, n):
    array.sort()
    l = [abs(n-i) for i in array]
    return array[l.index(min(l))]

# 두 수의 연산값 비교하기
def solution(a, b):
    return max(int(str(a)+str(b)), 2*a*b)

# k의 개수
def solution(i, j, k):
    s = ''
    for p in range(i,j+1):
        s += str(p)
    return s.count(str(k))

# 진료순서 정하기
def solution(emergency):
    answer = []
    for i in emergency:
        answer.append(sorted(emergency, reverse=True).index(i)+1)
    return answer

# 문자열 잘라서 정렬하기
def solution(myString):
    myString = myString.split('x')
    while '' in myString :
        myString.remove('')
    return sorted(myString)

# 문자열 반복해서 출력하기
a, b = input().strip().split(' ')
b = int(b)
print(a*b)



### 6/12
# 특별한 이차원 배열 1
def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer

# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    for i in my_string:
        if i.isalpha() == True:
            my_string = my_string.replace(i,' ')
    return sum(int(x) for x in my_string.split(' ') if len(x)>0)

    # 다른 풀이 : 정규식 사용 생각해볼 것

# 한 번만 등장한 문자
def solution(s):
    answer = ''
    for i in set(s):
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))

# 수 조작하기 2
def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i+1]-numLog[i] == 1 :
            answer += 'w'
        elif numLog[i+1]-numLog[i] == -1 :
            answer += 's'
        elif numLog[i+1]-numLog[i] == 10 :
            answer += 'd'
        else :
            answer += 'a'
    return answer

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    if x1== False and x2== False and x3== False and x4== False:
        return False
    if x1== False and x2== False:
        return False
    if x3== False and x4== False:
        return False
    return True

    # 다른사람 풀이
    # return (x1 | x2) & (x3 | x4)
    # sol = lambda x,y,z,w = (x or y) and (z or w)
    # return (x1 or x2) and (x3 or x4)

# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        if int(i[s:s+l]) > k :
            answer.append(int(i[s:s+l]))
    return answer

# 수열과 구간 쿼리 3
def solution(arr, queries):
    for i,j in queries:
        arr[i], arr[j] = arr[j],arr[i]
    return arr

# 문자열 뒤집기
def solution(my_string):
    my_string = list(my_string)
    return ''.join(my_string[::-1])

# 이진수 더하기
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]

# 1로 만들기
def solution(num_list):
    l = [0]*31
    l[1]=0
    l[2]=1
    
    for i in range(3,31):
        if i %2 ==0:
            l[i] = 1+l[i//2]
        else :
            l[i] = 1+l[(i-1)//2]

    answer = 0
    for i in num_list :
        answer += l[i]
        
    return answer



### 6/27
# 수열과 구간 쿼리 1
def solution(arr, queries):
    for i in queries:
        for j in range(i[0],i[1]+1):
            arr[j] += 1
    return arr

# 세로 읽기
def solution(my_string, m, c):
    l=[]
    answer = ''
    for i in range(0,len(my_string),m):
        l.append(list(my_string[i:i+m]))

    for i in range(len(l)):
        answer += l[i][c-1]
    return answer

    # # 스파이더에서는 돌아가는데 프로그래머스에서는 안돌아감
    # import numpy as np
    # def solution(my_string, m, c):
    #     l=[]
    #     answer = ''
    #     for i in range(0,len(my_string),m):
    #         l.append(list(my_string[i:i+m]))
    #     a = np.array(l)
    #     for i in range(len(a)):
    #         answer += a[i,c-1]
    #     return answer

# 컨트롤 제트
def solution(s):
    s = s.split(' ')
    answer = 0
    for i in range(len(s)):
        if s[i] == 'Z' :
            answer -= int(s[i-1])
        else :
            answer += int(s[i])
    return answer

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    if myString[-len(pat):] == pat :
        return myString
    
    for i in range(1,len(myString)+1):
        if myString[:-i][-len(pat):] == pat:
            return myString[:-i]

# 소인수분해
def solution(n):
    answer = []
    while n != 1 :
        for i in range(2,n+1):
            if n % i == 0:
                n = n//i
                answer.append(i)
                break
    return sorted(list(set(answer)))



### 6/28
# 공 던지기
def solution(numbers, k):
    if len(numbers)%2 == 0:
        l = [numbers[x] for x in range(0,len(numbers),2)]
        return l[int(k % (len(numbers)/2))-1]
    else:
        l = [numbers[x] for x in range(0,len(numbers),2)] + [numbers[x] for x in range(1,len(numbers),2)]
        return l[int(k % len(numbers))-1]
    
    # 다른 사람 풀이
    # def solution(numbers, k):
    #     return numbers[2 * (k - 1) % len(numbers)]

# 7의 개수
def solution(array):
    arr = ''
    for i in array:
        arr += str(i)
    return arr.count('7')

    # 다른 풀이
    # 바로 str(array).count('7') 해도됨

# 날짜 비교하기
def solution(date1, date2):
    if int(str(date1[0])+str(date1[1])+str(date1[2])) < int(str(date2[0])+str(date2[1])+str(date2[2])):
        return 1
    return 0

# 글자 지우기
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices,reverse=True) :
        my_string.pop(i)
    return ''.join(my_string)

# 특수문자 출력하기
print("!@#$%^&*(\\'\"<>?:;")



### 6/29
# 영어가 싫어요
def solution(numbers):
    d = {'zero' : '0', 'one' : '1', 'two' : '2',
         'three' : '3', 'four' : '4', 'five': '5',
         'six' : '6', 'seven' :'7' , 'eight' : '8', 'nine' : '9'}
    for i in d.keys():
        numbers = numbers.replace(i,d[i])
    return int(numbers)

# 세 개의 구분자
def solution(myStr):
    l = [x for x in myStr.replace('a','-').replace('b','-').replace('c','-').split('-') if len(x) > 0]
    if len(l) == 0:
        return ['EMPTY']
    else :
        return l
    
# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    return answer

# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    for i in range(min(len(board),k+1)):
        for j in range(min(len(board[i]),k-i+1)):
            answer += board[i][j]
    return answer

# 문자열 계산하기
def solution(my_string):
    return eval(my_string)



### 6/30
# 문자열 묶기
def solution(strArr):
    l = [len(i) for i in strArr]
    answer = 0
    for i in range(min(l),max(l)+1):
        answer = max(answer, l.count(i))
    return answer

# 조건에 맞게 수열 변환하기 2
def solution(arr):
    cnt = 0

    while True :
        arr1 = arr[:]
        for i in range(len(arr)) :
            if arr[i] >= 50 and arr[i]%2 == 0:
                arr[i] = arr[i]//2
            if arr[i] < 50 and arr[i]%2 != 0 :
                arr[i] = arr[i]*2 +1

        cnt += 1

        if arr1 == arr:
            return cnt-1
        
# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    answer = 0
    for i in range(0,len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer

# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True :
            answer += [arr[i]] * arr[i]*2
        else :
            answer = answer[:-arr[i]]
    return answer

# 구슬을 나누는 경우의 수
def solution(balls, share):
    answer = 1
    for i in range(balls-share+1, balls+1):
        answer *= i
    for i in range(1,share+1):
        answer /= i
    return int(answer)

    # combinations 쓰면 시간초과 뜸
    # from itertools import combinations
    # def solution(balls, share):
    #     return len(list(combinations([x for x in range(balls)], share)))



### 7/3
# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    sides = sorted(sides)
    for i in range(1,1+sides[1]):
        if i + sides[0]> sides[1]:
            answer += 1      
    for _ in range(sides[1]+1, sum(sides)):
            answer += 1      
    return answer

# 수열과 구간 쿼리 4
import math

def solution(arr, queries):
    for i in range(len(queries)):
        if queries[i][2] == 0 :
            pass
        else :
            for j in range(queries[i][2]*math.ceil(queries[i][0]/queries[i][2]),queries[i][1]+1,queries[i][2]):
                arr[j] += 1
    return arr

    # 답 비교

# 리스트 자르기
def solution(n, slicer, num_list):
    if n==1 :
        return num_list[:slicer[1]+1]
    elif n==2 :
        return num_list[slicer[0]:]
    elif n==3 :
        return num_list[slicer[0]:slicer[1]+1]
    else:
        return [num_list[i] for i in range(slicer[0],slicer[1]+1,slicer[2])]
    
# 외계어 사전
def solution(spell, dic):
    answer = [0]*len(dic)
    for i in spell:
        for j in range(len(dic)):
            if i in dic[j]:
                answer[j] += 1
    if answer.count(len(spell)) >= 1 :
        return 1
    else:
        return 2

# qr code
def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i %q ==r:
            answer += code[i]
    return answer




# a와 b 출력하기
a, b = map(int, input().strip().split(' '))
print('a =',a,'\nb =',b)

# 조건 문자열
def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            if n == m or n > m :
                return 1
            else:
                return 0
        elif eq == '!':
            if n > m :
                return 1
            else:
                return 0
    elif ineq == "<" :
        if eq == "=":
            if n == m or n < m :
                return 1
            else:
                return 0
        elif eq == '!':
            if n < m :
                return 1
            else:
                return 0

# 2의 영역
def solution(arr):
    if arr[-1] == 2:
        return arr[arr.index(2):]
    elif 2 in arr :
        return arr[arr.index(2):-arr[::-1].index(2)]
    elif 2 not in arr:
        return [-1]
    
# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    l = [2**x for x in range(11)]
    for i in l :
        if len(arr) <= i:
            return arr + [0] * (i-len(arr))
        
# 커피 심부름
def solution(order):
    answer = 0
    for i in order:
        if 'americano' in i:
            answer += 4500
        elif 'latte' in i :
            answer += 5000
        else :
            answer += 4500
    return answer



# 문자 개수 세기
def solution(my_string):
    answer = [0]*52

    for i in range(65,65+26):
        answer[i-65] = my_string.count(chr(i))
    
    for i in range(97,97+26):
        answer[i-97+26] = my_string.count(chr(i))
        
    return answer

# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    for s,e,k in queries :
        i = 0
        while i <= len(arr[s:e+1]) :
            if sorted(arr[s:e+1], reverse=True)[i] > k:
                i += 1
            else :
                if i == 0 :
                    answer.append(-1)
                else :
                    answer.append(sorted(arr[s:e+1], reverse=True)[i-1])
                break
    return answer

    ### 이거 왜 런타임에러? 왜 안돌아가는지 모르겠네

# 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0,0]
    key = ['up', 'down','left','right']
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for k in keyinput:
        i = key.index(k)
        if abs(answer[0] + dx[i]) <= (board[0]-1)/2 and abs(answer[1] + dy[i]) <= (board[1]-1)/2 :
            answer = [answer[0] + dx[i], answer[1] + dy[i]]
        else :
            pass
    return answer

# 직사각형 넓이 구하기
def solution(dots):
    for i in range(1,4):
        if dots[0][0] == dots[i][0]:
            a = abs(dots[0][1]-dots[i][1])
        else :
            b = abs(dots[0][0]-dots[i][0])
    return a*b

# 종이 자르기
def solution(M, N):
    return (M-1) + (N-1)*M

# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string[:] + my_string[s+len(overwrite_string):]

# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        elif stk != [] and stk[-1] >= arr[i] :
            stk.pop()
    return stk

# 로그인 성공?
def solution(id_pw, db):
    for id, pw in db:
        if id == id_pw[0]:
            if pw == id_pw[1]:
                return 'login'
            else :
                return 'wrong pw'
    return 'fail'

# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while chicken // 10 !=0:
        answer += chicken // 10
        chicken = chicken//10 + chicken%10
    return answer

# 두 수의 합
def solution(a, b):
    return str(int(a)+int(b))

# 등수 매기기
def solution(score):
    answer = []
    avg = []
    for i,j in score :
        avg.append((i+j)/2)
    for i in range(len(avg)):
        answer.append(sorted(avg, reverse = True).index(avg[i])+1)
    return answer

    # 순위 함수 : pandas의 rank함수

# 유한소수 판별하기

# 대소문자 바꿔서 출력하기
str = list(input())
for i in range(len(str)):
    if str[i].isupper() == True:
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
print(''.join(str))

    # swapcase 기억하기

# 저주의 숫자 3
def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer += 1
        if answer % 3 == 0 or '3' in str(answer) :
            while answer % 3 == 0 or '3' in str(answer) :
                answer += 1
    return answer

# 특이한 정렬
def solution(numlist, n):
    answer = []
    numlist = sorted(numlist, reverse=True)
    l = []
    # 거리계산
    for i in numlist:
        l.append(abs(i-n))
    # 결과찾기
    while len(l) != 0:
        answer.append(numlist[l.index(min(l))])
        numlist.pop(l.index(min(l)))
        l.remove(min(l))
    return answer

# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    for s,e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

# 문자열 밀기
def solution(A, B):
    for i in range(len(A)):
        if A == B :
            return i
        A = A[-1] + A[:-1]
    return -1

# 정사각형으로 만들기
def solution(arr):
    if len(arr) == len(arr[0]) :
        pass
    elif len(arr) > len(arr[0]) :
        for i in range(len(arr)) :
            arr[i] = arr[i] + [0]*(len(arr) - len(arr[i]))
    elif len(arr) < len(arr[0]) :
        for _ in range(len(arr[0]) - len(arr)):
            arr.append([0]*len(arr[0]))
    return arr

# 왼쪽 오른쪽
def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []
    else :
        if 'l' not in str_list :
            return str_list[str_list.index('r')+1:]
        elif 'r' not in str_list:
            return str_list[:str_list.index('l')]
        elif str_list.index('l') < str_list.index('r'):
            return str_list[:str_list.index('l')]
        else :
            return str_list[str_list.index('r')+1:]
        
# 그림 확대
def solution(picture, k):
    answer = []
    for pic in picture:
        a = ''
        for i in range(len(pic)):
            a += pic[i]*k
        for _ in range(k):
            answer.append(a)
    return answer

    # 답비교

# 무작위로 K개의 수 뽑기
# 다항식 더하기
# 배열 만들기 6
def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
            i += 1
        elif answer != [] and answer[-1] ==arr[i]:
            answer.pop()
            i+=1
        elif answer != [] and answer[-1] != arr[i] :
            answer.append(arr[i])
            i+=1
    if answer != []:
        return answer
    else:
        return [-1]

# 전국 대회 선발 고사
# 최빈값 구하기


# 배열 만들기 2
# 문자열 출력하기
# OX퀴즈
# 코드 처리하기
# 분수의 덧셈


# 다음에 올 숫자
# 연속된 수의 합
# 안전지대
# 겹치는 선분의 길이
# 주사위 게임 3


# 평행
# 배열 조각하기
# 정수를 나선형으로 배치하기
# 옹알이 (1)
from itertools import permutations

data = ['aya','ye','woo','ma']
a=[]


def solution(babbling):
    for i in range(1,len(data)+1):
        p = list(permutations(data,i))
        
        for j in range(len(p)):
            a.append(''.join(p[j]))
    
    answer= 0
    
    for i in range(len(babbling)):
        for j in range(len(a)):
            if babbling[i] == a[j]:
                answer += 1
                
    
    return answer