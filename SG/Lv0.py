# 5월 11일
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

# 5월 12일
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

#5월 15일
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

# 5월 17일 
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
    
# 5월 18일
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


# 5월 19일
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


# 5월 22일 
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


# 5월 24일
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