'''0511'''
# 두 수의 곱
def solution(num1, num2):
    return num1 * num2

# 몫 구하기 
def solution(num1, num2):
    return num1%num2

# 두 수의 차
def solution(num1, num2):
    return num1-num2

# 나머지 구하기
def solution(num1, num2):
    return num1//num2

# 나이 출력
def solution(age):
    return (2022 - age)+1

'''0512'''
# 두 수의 합
def solution(num1, num2):
    return num1+num2

# 두 수의 나눗셈
def solution(num1, num2):
    return int((num1/num2)*1000)

# 각도기
def solution(angle):
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
            
    return answer

    # answer = lambda x: 1 if angle>0 and angle <90 else (2 if angle==90 else (3 if angle > 90 and angle < 180 else 4))
    # return answer(angle)

# 짝수의 합
def solution(n):
    return sum(x for x in range(n+1) if x%2==0)

# 배열의 평균 값
def solution(numbers):
    return sum(x for x in numbers)/len(numbers)

'''0515'''
# 양꼬치
def solution(n, k):
    free = len([x for x in range(n+1) if x!=0 and x%10==0])
    answer = n*12000 + ((k-free)*2000)
    return answer

# n의 배수
def solution(num, n):
    answer = lambda x, y: 1 if x%y==0 else 0
    return answer(num,n) 

# 정수 부분
def solution(flo):
    return int(flo)

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

# 문자열로 변환
def solution(n):
    return str(n)

'''0517'''
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
    answer = lambda i,j,k: 1 if i%j==0 and i%k==0 else 0
    return answer(number, n, m)

'''0518'''
# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    x = lambda a,b,f: a+b if flag==True else a-b
    return x(a,b,flag)

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    else: return 0

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    c = lambda arr, k: [a+k for a in arr] if k%2==0 else [a*k for a in arr] 
    return c(arr,k)

# 배열 두 배 만들기
def solution(numbers):
    answer = [x*2 for x in numbers]
    return answer

# 문자열 곱하기
def solution(my_string, k):
    return my_string*k

'''0519'''
# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
    
# 점의 위치 구하기
def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            return 1
        else: return 4
    else:
        if dot[-1]>0:
            return 2
        else: return 3

# 편지
def solution(message):
    return len(message)*2

'''0522'''
# 배열 원소의 길이
def solution(strlist):
    answer = [len(x) for x in strlist]
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

# 피자 나눠 먹기 (3)
from math import ceil

def solution(slice, n):
    return ceil(n/slice)

# 피자 나눠 먹기 (1)
from math import ceil
def solution(n):
    return ceil(n/7)

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for x in numbers: 
        if answer <=n:
            answer+=x
    return answer

'''0524'''
# 중앙값 구하기
def solution(array):
    return sorted(array)[len(array)//2]

# 순서쌍의 개수
def solution(n):
    answer = len([x for x in range(1,n+1) if n%x==0])
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = len([x for x in array if x>height]) 
    return answer

# 중복된 숫자 개수
def solution(array, n):
    answer = len([x for x in array if x==n])
    return answer

# 최댓값 만들기(1)
def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-1]*numbers[-2]

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# 삼각형의 완성조건 (1)
def solution(sides):
    sides = sorted(sides)
    if sides[-1] < sides[0]+sides[1]:
        return 1
    else: return 2

# 문자열 뒤집기
def solution(my_string):
    answer = ''.join(list(my_string)[::-1])
    return answer

# 짝수 홀수 개수
def solution(num_list):
    even, odd = 0,0
    for x in num_list:
        if x%2==0:
            even+=1
        else: odd+=1
    return [even,odd]

# 길이에 따른 연산
from math import prod
def solution(num_list):
    answer = lambda x: sum(i for i in x) if len(x)>=11 else prod(i for i in x)
    return answer(num_list)

'''0525'''
# 옷가게 할인 받기
def solution(price):
    answer = lambda price: price-(price*0.05) if price>=100000 and price<300000 else (price-(price*0.1) if price>=300000 and price<500000 else (price-(price*0.2)) if price>=500000 else price)
    return int(answer(price))

# 아이스 아메리카노
def solution(money):
    cups=0
    while money>=5500:
        money = money - 5500
        cups+=1
    return [cups, money]

# 첫 번째로 나오는 음수
def solution(num_list):
    for i, n in enumerate(num_list):
        if n<0:
            return i
    return -1

# 모음 제거
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for v in vowels:
        if v in my_string:
            my_string = my_string.replace(v,'')
    return my_string

# 원소들의 곱과 합
from math import prod
def solution(num_list):
    answer = lambda num: 1 if prod(num) < sum(num)**2 else 0
    return answer(num_list)

# 정수 찾기
def solution(num_list, n):
    if n in num_list:
        return 1
    else: return 0

# 주사위 게임 1
def solution(a, b):
    if a%2!=0 and b%2!=0:
        return a**2 + b**2
    elif a%2!=0 or b%2!=0:
        return 2*(a+b)
    elif a%2==0 and b%2==0:
        return abs(a-b)
    
# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# 뒤에서 5등 위로
def solution(num_list):
    answer = sorted(num_list)[5:]
    return answer

# 공백으로 구분하기 1
def solution(my_string):
    answer = my_string.split(' ')
    return answer

'''0526'''
# rny_string
def solution(rny_string):
    answer = rny_string.replace('m', 'rn')
    return answer

# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for s in s1:
        if s in s2:
            answer+=1
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer = answer+(s*n)
    return answer

# 자릿수 더하기
def solution(n):
    answer = sum([int(x) for x in str(n)])
    return answer

# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

# 짝수는 싫어요
def solution(n):
    answer = [x for x in range(1,n+1) if x%2!=0]
    return answer

# 카운트 업
def solution(start, end):
    answer = [x for x in range(end+1) if x>=start]
    return answer

# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    else: return 0

# 카운트 다운
def solution(start, end):
    answer = [n for n in range(start+1) if n>=end][::-1]
    return answer

# n개 간격의 원소들
def solution(num_list, n):
    answer = [x for i,x in enumerate(num_list) if i%n==0]
    return answer

'''0529'''
# 문자열 정수의 합
def solution(num_str):
    answer = sum(int(x) for x in num_str)
    return answer

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = sum([int(x) for x in my_string if x.isdigit()])
    return answer

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1+str2)

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for x in index_list:
        answer += answer.join(my_string[x])
    return answer

# 원하는 문자열 찾기
def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else: return 0

# 배열 만들기 1
def solution(n, k):
    answer = [x for x in range(1,n+1) if x%k==0]
    return answer

# 홀짝 구분하기
a = int(input())

if a%2==0:
    print(a,"is even")
else:
    print(a, "is odd")

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer = []
    for a in arr:
        if a<50 and a%2!=0:
            answer.append(a*2)
        elif a>=50 and a%2==0:
            answer.append(a/2)
        else: answer.append(a)
    return answer

# 수 조작하기 1
''' 아니 이 왜 안 되는거?? 내 이해 못함???? '''
def solution(n, control):
    answer =  n + (control.count('w')*1) - (control.count('s')*1) + (control.count('d')*10) - (control.count('a')*10) 
    
    return answer

# 뒤에서 5등까지
def solution(num_list):
    answer = sorted(num_list)[:5]
    return answer

'''0530'''
# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    # answer = [x.lower() for i,x in enumerate(strArr) if i%2!=0]
    answer = []
    for i, x in enumerate(strArr):
        if i%2==0:
            answer.append(x.lower())
        else:
            answer.append(x.upper())
    return answer

# 문자열안에 문자열
def solution(str1, str2):
    answer = lambda a, b: 1 if b in a else 2
    return answer(str1, str2)

# 제곱수 판별하기
from math import sqrt
def solution(n):
    if n%sqrt(n)==0: return 1
    else: return 2

# 이어 붙인 수
def solution(num_list):
    even=''
    odd=''
    for n in num_list:
        if n%2==0:
            even+=str(n)
        else: odd+=str(n)
    return int(even)+int(odd)

# 문자열 바꿔서 찾기
def solution(myString, pat):
    if pat in myString.replace('A','C').replace('B', 'A').replace('C', 'B'): return 1
    else:  return 0

# 개미 군단
def solution(hp):
    answer = 0
    while hp > 0:
        if hp<3:
            hp-=1
            answer+=1
        elif hp>=3 and hp<5:
            hp-=3
            answer+=1
        elif hp>=5:
            hp-=5
            answer+=1
    return answer

# 문자열 바꿔서 찾기
def solution(myString, pat):
    if pat in myString.replace('A','C').replace('B', 'A').replace('C', 'B'): return 1
    else:  return 0
    
# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 0
    if len(is_prefix) > len(my_string):
        return 0
    else:
        for i,x in enumerate(is_prefix):
            if my_string[i]==x:
                answer=1
            else:
                answer=0
                break
        
    return answer

# 더 크게 합치기
def solution(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    if ab > ba: return ab
    else: return ba

# 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    return num_list

'''0531'''
# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if ex in s:
            pass
        else:
            answer += s
    return answer

# 암호 해독
def solution(cipher, code):
    answer = ''
    for i,x in enumerate(cipher):
        if (i+1)%code==0:
            answer+=x
    return answer

# 가위 바위 보
def solution(rsp):
    answer = ''
    for n in rsp:
        if n=='2':
            answer+='0'
        elif n=='0':
            answer+='5'
        elif n=='5':
            answer+='2'
    return answer

# 세균 증식
def solution(n, t):
    for i in range(t):
        n=n*2
    return n

# 홀짝에 따라 다른 값 반환하기
def solution(n):
    if n%2==0:
        return sum([x**2 for x in range(1,n+1) if x%2==0])
    else:
        return sum([x for x in range(1,n+1) if x%2!=0])
    
# 대문자와 소문자
def solution(my_string):
    return my_string.swapcase()

# 주사위의 개수
def solution(box, n):
    l = box[0]//n
    w = box[1]//n
    h = box[2]//n
    return l*w*h

# 공백으로 구분하기 2
def solution(my_string):
    return my_string.split()

# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(a,"+",b,"=",a+b)

# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for x in arr:
        for i in range(x):
            answer.append(x)
    return answer


'''0601'''
# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i,s in enumerate(my_strings):
        answer+=s[parts[i][0]:parts[i][1]+1]
    return answer

# 직각삼각형 출력하기
n = int(input())
for i in range(1,n+1):
    print('*'*i)

# 문자열 정렬하기 (1)
def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdigit()])

# 최댓값 만들기 (2)
def solution(numbers):
    numbers = sorted(numbers)
    if numbers[0]*numbers[1]>numbers[-1]*numbers[-2]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]


# 홀수 vs 짝수
def solution(num_list):
    even=0
    odd=0
    for i, n in enumerate(num_list):
        if i%2==0:
            even+=n
        else:
            odd+=n
    if even < odd:
        return odd
    else: return even

# n의 배수 고르기
def solution(n, numlist):
    answer = [x for x in numlist if x%n==0]
    return answer

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    answer = []
    for i, a in enumerate(arr):
        if len(arr)%2!=0:
            if i%2==0:
                answer.append(a+n)
            else:
                answer.append(a)
        elif len(arr)%2==0:
            if i%2!=0:
                answer.append(a+n)
            else:
                answer.append(a)
            
    return answer

# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = 0
    my_string=my_string[::-1]
    if len(is_suffix) > len(my_string):
        return 0
    else:
        for i, x in enumerate(is_suffix[::-1]):
            if my_string[i]==x:
                answer=1
            else:
                answer-0
                break
    return answer

# A 강조하기
def solution(myString):
    return myString.lower().replace('a','A')

# 배열 회전시키기
def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,numbers[-1])
        numbers=numbers[:-1]
        
    else:
        numbers.append(numbers[0])
        numbers=numbers[1:]
    return numbers
        


'''0602'''
# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer =''
    for i, x in enumerate(my_string):
        if i==num1:
            answer+=my_string[num2]
        elif i==num2:
            answer+=my_string[num1]
        else:
            answer+=my_string[i]
    return answer

# 외계행성의 나이
def solution(age):
    answer = ''
    x ={0: 'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    for n in str(age):
        answer+=x[int(n)]
        # x[1] -> 'b'
        # x[2] -> 'c'
    return answer

# 가장 큰 수 찾기
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer

# 접미사 배열
def solution(my_string):
    answer = []
    for s in range(len(my_string)):
        answer.append(my_string[s:])
    return sorted(answer)

# 피자 나눠 먹기 (2)
def solution(n):
    answer = 0
    pan = 6
    while True:
        if pan%n==0:
            answer+=1
            break
        else:
            pan+=6
            answer+=1
    return answer

# 0 떼기
def solution(n_str):
    answer = str(int(n_str))
    # '00000001' -> 1
    return answer

# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i, x in enumerate(str1):
        answer+=str1[i]
        answer+=str2[i]
    return answer

# 369게임
def solution(order):
    answer = str(order).count('3') + str(order).count('6') +str(order).count('9')
    return answer

# 5명씩
def solution(names):
    answer = []
    for i, x in enumerate(names):
        if i%5==0:
            answer.append(x)
    return answer

# l로 만들기
def solution(myString):
    answer = ''
    for s in myString:
        if ord(s) < ord('l'):
            answer+='l'
        else:
            answer+=s
    return answer


#0603
# 약수 구하기
def solution(n):
    answer = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            answer.append(i)
    answer.append(n)
    return answer

# 문자열 돌리기
str = input()
for s in str:
    print(s)

# 배열 비교하기
def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        if sum(arr1)<sum(arr2):
            return -1
        elif sum(arr1)>sum(arr2):
            return 1
        else: return 0

# 숫자 찾기
def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k))+1
    else: return -1

# ad 제거하기
def solution(strArr):
    answer = []
    for s in strArr:
        if 'ad' in s:
            pass
        else:
            answer.append(s)
    return answer

# 할 일 목록
def solution(todo_list, finished):
    answer=[todo_list[i] for i, f in enumerate(finished) if f==False]
    return answer

# 간단한 식 계산하기 eval()쓰자
def solution(binomial):
    a = int(binomial.split()[0])
    b = int(binomial.split()[2])
    op = binomial.split()[1]
    
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else: return a*b

# 콜라츠 수열 만들기
def solution(n):
    answer = [n]
    while n!=1:
        if n%2==0:
            n=n/2
            answer.append(n)
        else:
            n=3*n+1
            answer.append(n)
    return answer

# 배열의 원소 삭제하기
def solution(arr, delete_list):
    answer = []
    for a in arr:
        if a in delete_list:
            pass
        else:
            answer.append(a)
    return answer

# 문자열 정렬하기 (2)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))


#0604
# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(n+1):
        if len(hap(i)) >= 3:
            answer+=1
    return answer
def hap(n):
    answer = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            answer.append(i)
    answer.append(n)
    return answer

# 가까운 1 찾기
def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if arr[i]==1 and i>=idx:
            return i
    return answer

# 주사위 게임 2
def solution(a, b, c):
    if a!=b and a!=c and b!=c:
        return a+b+c
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
        return (a+b+c)*(a**2+b**2+c**2)
    elif a==b==c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)

# 특별한 이차원 배열 2
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==arr[j][i]:
                answer=1
            elif arr[i][j]!=arr[j][i]:
                return 0
            
    return answer

# 순서 바꾸기
def solution(num_list, n):
    answer= num_list[n:]+num_list[:n]
    return answer

# 9로 나눈 나머지
def solution(number):
    answer = int(number)%9
    return answer

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer+=s
    return answer

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
    for l in letter.split():
        answer += ''.join(morse[l])
    return answer

# x 사이의 개수
def solution(myString):
    answer = []
    count=0
    for s in myString:
        if s!='x':
            count+=1
        else:
            answer.append(count)
            count=0
    answer.append(count)
    return answer

# 배열 만들기 3
def solution(arr, intervals):
    a = []
    for i in intervals:
        a.append(arr[i[0]:i[1]+1])
    answer = [x for x in a for x in x]
    return answer

# 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)\
    
# 날짜 비교하기
def solution(date1, date2):
    d1=int(str(date1[0])+str(date1[1])+str(date1[2]))
    d2=int(str(date2[0])+str(date2[1])+str(date2[2]))
    if d1<d2:
        return 1
    else: return 0

# 숨어있는 숫자의 덧셈(2)
def solution(my_string):
    answer=0
    new_string=''
    
    for s in my_string:
        if s.isalpha() == True:
            new_string+='x'
        else:
            new_string+=s

    new_string=new_string.split('x')
    
    for n in new_string:
        if n =='':
            continue
        else:
            answer += int(n)
    return answer

# 1로 만들기
def solution(num_list):
    answer = 0
    for num in num_list:
        while num>1:
            if num%2==0:
                num = num/2
                answer+=1
            else:
                num =(num-1)/2
                answer+=1
    return answer

# 조건에 맞게 수열 변환하기 2
def solution(arr):
    answer = 0
    while True:
        new_arr=[]
        for a in arr:
            if a >= 50 and a%2==0:
                a=a/2
                new_arr.append(a)
            elif a<50 and a%2!=0:
                a=(a*2)+1
                new_arr.append(a)
            else:
                new_arr.append(a)
        answer+=1
        if arr == new_arr:
            break
        arr=new_arr
        
    return answer-1

# 수열과 구간 쿼리 1
def solution(arr, queries):
    for i, j in queries:
        for n in range(i,j+1):
            arr[n]+=1
    return arr

# 세로 읽기
def solution(my_string, m, c):
    answer = ''
    for i,s in enumerate(my_string):
        if i%m == c-1:
            answer+=s   
    return answer

# 컨트롤 제트
def solution(s):
    arr =[]
    for a in s.split(' '):
        if a=='Z':
            arr.pop()
        else:
            arr.append(int(a))
    return sum(arr)

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    answer = ''
    splt = myString.split(pat)
    for i, x in enumerate(splt):
        if i!=len(splt)-1:
            answer+=x
            answer+=pat
    return answer

# 소인수분해
def solution(n):
    answer = []
    i=2
    while i<=n:
        if n%i==0:
            if i not in answer:
                answer.append(i)
            n//=i
        else:
            i+=1
    
    return (answer)



# 공 던지기
def solution(numbers, k):
    if len(numbers) % 2 == 0:
        evens = []
        for x in range(0,len(numbers),2):
            evens.append(numbers[x])
        return evens[(k%len(evens)) - 1]
    elif len(numbers) % 2 != 0:
        odds = []
        for i in range(2):
            for x in range(i,len(numbers),2):
                odds.append(numbers[x])
        return odds[(k%len(odds)) - 1]

# 7의 개수
def solution(array):
    answer = 0
    tmp=''
    for num in array:
        tmp+=str(num)
        
    return tmp.count('7')

# 날짜 비교하기
def solution(date1, date2):
    answer = 0
    d1=int(str(date1[0])+str(date1[1])+str(date1[2]))
    d2=int(str(date2[0])+str(date2[1])+str(date2[2]))
    if d1<d2:
        return 1
    else: return 0
    # print(d1)
    # return answer

# 글자 지우기
def solution(my_string, indices):
    answer = ''
    for i,x in enumerate(my_string):
        if i not in indices:
            answer+=x    
    return answer

# 특수문자 출력하기
print('!@#$%^&*(\\\'\"<>?:;')


# 영어가 싫어요
def solution(numbers):
    dic = {'ze':'0', 'on':'1', 'tw':'2', 'th':'3', 'fo':'4', 'fi':'5', 'si':'6', 'se':'7', 'ei':'8', 'ni':'9'}
    tmp=''
    for i, _ in enumerate(numbers):
        if i != len(numbers)-1:
            if numbers[i]+numbers[i+1] in dic:
                tmp+=dic[numbers[i]+numbers[i+1]]
    answer = int(tmp)
    return answer

# 세 개의 구분자
def solution(myStr):
    answer = []
    for x in myStr.replace('a','`').replace('b','`').replace('c','`').split('`'):
        if x!='':
            answer.append(x)
    if answer == []:
        return ["EMPTY"]
    else: return answer

# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    ind=[]
    for i in range(0, len(my_str), n):
        ind.append(i)
    for i, x in enumerate(ind):
        if i<len(ind)-1:
            answer.append(my_str[ind[i]:ind[i+1]])
    answer.append(my_str[ind[-1]:])
    return answer

# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    for i,b in enumerate(board):
        for j, x in enumerate(b):
            if i+j<=k:
                answer+=x
    return answer

# 문자열 계산하기
def solution(my_string):
    split = my_string.split()
    answer = int(split[0])
    for i, s in enumerate(split):
        if i<len(split)-1 and i!=0:
            if s == '+':
                answer+=int(split[i+1])
            elif s== '-':
                answer-=int(split[i+1])
            else:
                continue
    return answer


# 문자열 묶기   ##웨안돼!
def solution(strArr):
    l = [len(x) for x in strArr]
    dic={}
    for i in l:
        if i not in dic:
            dic[i]=l.count(i)
    answer = max([k for k, v in dic.items() if v==max(dic.values())])
    print([k for k, v in dic.items()],[v for k, v in dic.items()])
    print([k for k, v in dic.items() if v==max(dic.values())])
    print(max([k for k, v in dic.items() if v==max(dic.values())]))
    return answer

# 조건에 맞게 수열 변환하기 2
def solution(arr):
    answer = 0
    while True:
        new_arr=[]
        for a in arr:
            if a >= 50 and a%2==0:
                a=a/2
                new_arr.append(a)
            elif a<50 and a%2!=0:
                a=(a*2)+1
                new_arr.append(a)
            else:
                new_arr.append(a)
        answer+=1
        if arr == new_arr:
            break
        arr=new_arr
        
    return answer-1

# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    answer = 0
    l = len(pat)
    for i,s in enumerate(myString):
        if i<=len(myString)-l:
            if s==pat[0]:
                if myString[i:i+l]==pat:
                    answer+=1
    return answer

# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for i,f in enumerate(flag):
        if f == True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for i in range(arr[i]):
                if answer==[]:
                    pass
                else:
                    answer.pop()
                
            
    return answer

# 구슬을 나누는 경우의 수


# 삼각형의 완성조건 (2)
# 수열과 구간 쿼리 4
def solution(arr, queries):
    for i, _ in enumerate(arr):
        for q in queries:
            if i>=q[0] and i<=q[1] and i%q[2]==0:
                arr[i]+=1
    return arr

# 리스트 자르기 ##시ㄹ패!!!
def solution(n, slicer, num_list):
    answer=[]
    if n==1:
        answer = num_list[:slicer[1]+1]
    elif n==2:
        answer = num_list[slicer[1]:]
    elif n==3:
        answer = num_list[slicer[0]:slicer[1]+1]
    elif n==4:
        tmp = num_list[slicer[0]:slicer[1]+1]
        for i, x in enumerate(tmp):
            if i%slicer[2]==0:
                answer.append(x)
        
    return answer

# 외계어 사전
# qr code

# 수열과 구간 쿼리 2
def solution(arr, queries):
    ans=[]
    for s, e, k in queries:
        m=[]
        for i in range(s,e+1):
            if arr[i] > k:
                m.append(arr[i])
            else:
                pass
        if len(m)!=0:
            ans.append(min(m))
        else:
            ans.append(-1)
    return ans

# 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0,0]
    maxx = board[0]//2
    maxy = board[1]//2
    for k in keyinput:
        if k == 'left':
            if answer[0]>-maxx:
                answer[0] -=1
        elif k == 'right':
            if answer[0]<maxx:
                answer[0]+=1
        elif k == 'up':
            if answer[1]<maxy:
                answer[1]+=1
        elif k == 'down':
            if answer[1]>-maxy:
                answer[1]-=1
    return answer

# 유한소수 판별하기
from fractions import Fraction
from decimal import *

def solution(a, b):
    x = str(Fraction(a,b)).split('/')
    b = fac(int(x[1]))
    
    for k in b:
        if k not in [2,5]:
            return 2
        else: return 1

def fac(x):
    tmp=[]
    i = 2
    while i <= x:
        if x % i == 0:
            tmp.append(i)
            x = x / i
        else:
            i += 1
    return tmp

# 오른쪽 왼쪽
def solution(str_list):
    for s in str_list:
        if s =='l':
            return str_list[:str_list.index(s)]

        elif s =='r':
            return str_list[str_list.index(s):]
    return []