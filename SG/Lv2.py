# 5월 11일
# 최댓값과 최솟값
def solution(s):
    a=s.split()                     #.split(): 문자열을 리스트로 변환
    for i in range(len(a)):
        a[i]=int(a[i])                          
    return str(min(a)) + " " + str(max(a))

# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    a = s.split(' ')                  #''안에 공백이 있어야 함
    for i in range(len(a)): 
        a[i]=a[i].capitalize()       #capitalize: 첫번째 문자만 대문자로 변환
    answer=' '.join(a)               #join(): 리스트를 문자로 변환
    return answer

# 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort()                          #sort(): 오름차순 정렬
    B.sort()
    n=len(A)
    for i in range(n):
        answer += A[i]*B[n-i-1]
    return answer

# 5월 12일 
# 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack ==[]:              # ")" 넣기 전 이미 비어있으면 F
                return False
            else:
                stack.pop()             # "(" 들어가 있으면 빼기
    if stack != []:                     # 다 했는데 남아있는게 있으면 F
        return False
    return True

# 이진 변환 만들기
def solution(s):
    answer = []
    cnt=0
    zero=0
    while 1:
        if s == "1":
            break
        cnt += 1
        zero += s.count("0")
        s = s.replace("0", "")
        new = len(s)
        s = bin(new)[2:]
    answer.append(cnt)
    answer.append(zero)
    return answer

# 숫자의 표현
def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            if (j-i+1)*(i+j)/2 ==n:
                answer += 1
            if (j-i+1)*(i+j)/2 > n:
                break
    return answer


# 5월 15일
# 다음 큰 숫자
def solution(n):
    cnt = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == cnt:
            return i
        
# 피보나치 수
def solution(n):
    a = 1
    b = 1
    if n == 1 or n ==2 :
        return 1
    for i in range(1,n) : 
        a , b = b , b+a                 # 바뀐 값을 사용하기 때문에 동시 작업 필요
    return a % 1234567

# 짝지어 제거하기
def solution(s):
    stack = []                          # 스택 활용
    for i in s:
        if stack ==[]:
            stack.append(i)
        else :
            if i == stack[-1]:
                stack.pop()
            else :
                stack.append(i)
    if stack != [] :
        return 0
    else :
        return 1
    

# 5월 17일
# 영어 끝말잇기
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] :
            return [(i%n)+1, (i//n)+1]
        elif words[i] in words[:i]:            # enumerate로 푸는 방법,,
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(0,5000):                     # 범위 이게 최선이야?
        for j in range(0,5000):
            if i+j == (brown-4)/2 and i*j == yellow:
                return [j+2,i+2]

# 구명보트


# 5월 18일
# 예상 대진표
def solution(n,a,b):
    answer = 0
    while a != b :
        if a%2 == 1:
            a = a//2+1
        else:
            a = a//2
        if b%2==1:
            b = b//2+1
        else:
            b = b//2
        answer += 1
    return answer

# 점프와 순간 이동 - while문
def solution(n):
    cnt = 0
    while n != 0:
        if n%2==0:
            n = n/2
        else:
            n -= 1
            cnt += 1
    return cnt

# 점프와 순간 이동 - while문의 원리가 2진수 바꾸는 법
def solution(n):
    return bin(n).count('1')

# N개의 최소공배수
def solution(arr):
    def lcm(a, b):
        for i in range(max(a, b), (a * b) + 1):
            if i % a == 0 and i % b == 0:
                return i
    for j in range(0,len(arr)-1):              # 앞에서 두 개씩 최소공배수 구하기
        arr[j+1] = lcm(arr[j],arr[j+1])
    return(arr[-1])


# 5월 19일
# 멀리 뛰기
def solution(n):
    answer = [1,2]
    for i in range(2,n+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-2]%1234567               # 피보나치..

# 귤 고르기



# 5월 22일 
# H-Index
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer = i+1
    return answer

# 연속 부분 수열 합의 개수
def solution(elements):
    answer = []
    two = elements+elements
    for i in range(0,len(elements)):
        for j in range(0,len(elements)+1):
            answer.append(sum(two[i:i+j]))        
    return len(set(answer))-1               # 너무 오래 걸림..


# 괄호 회전하기

# [1차] 캐시

# 행렬의 곱셈    
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for m in range(len(arr1))]
    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# n^2 배열 자르기


# 의상 
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    for i in dic.keys():
        answer *= dic[i] +1
    return answer-1

# 튜플
def solution(s):
    str = s[2:-2].split('},{')
    str.sort(key=lambda x : len(x))
    answer = []
    result = []
    for i in str:
        i = list(map(int, i.split(",")))  
        answer.append(i)
          
    for j in answer:
        for k in j:
            if k not in result:
                result.append(k)
    return result
        

# 기능 개발
import math
def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    answer = []
    
    temp = days[0]
    cnt = 0
    
    for day in days:
        if day <= temp:
            cnt+=1
        else:
            answer.append(cnt)
            cnt = 1
            temp = day            
    answer.append(cnt)
    
    return answer

 


# 프로세스



# [1차] 뉴스 클러스터링
def solution(str1, str2):
    set1 = [str1.lower()[i]+str1.lower()[i+1] for i in range(0,len(str1)-1)]
    set2 = [str2.lower()[i]+str2.lower()[i+1] for i in range(0,len(str2)-1)]
    
    new_set1 = [i for i in set1 if i.isalpha()]
    new_set2 = [i for i in set2 if i.isalpha()]
    
    #교집합 만들기
    intersection = []
    temp = new_set2.copy() #얕은 복사
    for i in new_set1:
        if i in temp:
            temp.remove(i)
            intersection.append(i)
            
    if new_set1 == new_set2:
        return 65536
    else:
        union = len(new_set1) + len(new_set2) - len(intersection)
        return int((len(intersection)/union)*65536)
    


# 할인행사 
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for j in range(len(discount)-9):
        if dic == Counter(discount[j:j+10]): 
            answer += 1
    return answer



# 배열 나누기               # 아닌거 같은데 답은 나옴...
def solution(arr):
    cnt = 0
    
    for i in range(len(arr)):
        for k in range(0,len(arr)):
            if sum(arr[k:]) == sum(arr[:k]):
                if arr[k:]!=[] and arr[:k]!=[]:
                    print(arr[k:],arr[:k])
                    cnt += 1
                
            else:
                for j in range(i+1, len(arr)):
                    if arr[i] != arr[j]:
                        arr[i],arr[j]=arr[j],arr[i]
                
    return cnt



# 고정지출
def sol(k,arr):
    answer = []
    dic = {}
    result = []
    
    #형태 바꾸기
    for i in range(0,len(arr)):
        arr[i] = list(map(int,arr[i].replace('.',' ').split()))
    
    #날짜 정렬 해가 바뀌는 것도 있으니까 
    for m in arr:
        answer.append([(m[0]-arr[0][0])*12+m[1],m[2],m[3]])
        
    month = list(range(answer[-1][0]-k+1,answer[-1][0]+1))
       
    
    for k in answer:
        if k[0] in month:
            result.append(k)
   
    # 개수 세기
    for item in result:
        day = item[1]
        money = item[2]
        if (day,money) in dic:
            dic[(day,money)] += 1
        else:
            dic[(day,money)] = 1
                      
    data = [key for key, value in dic.items() if value >= 3]     
    return data