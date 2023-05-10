
def recursive(n):
    if n<=1:
        return 1
    
    return n * recursive(n-1)



from collections import deque

a = deque('3')
a



b=deque([2])
b
b.append(4)
b

help(deque)
dir(deque)


# https://wikidocs.net/105044


# 퀵정렬
def quick(array, start, end):
    if start >= end:
        return
    
    
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
array

array_sort = sorted(array)
array_sort

### 입력 코드
a,b = map(int, input().split())
c = list(map(int, input().split()))


array = [('홍길동',95), ('lee',77)]

array = sorted(array, key = lambda student : student[1])
array

## 이진탐색

def bina(array, target, start, end):
    while start <= end :
        mid = (start + end) //2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1

    return None



def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


from itertools import cycle
a=cycle(['a','b','c'])
next(a)


## two pointers
n=5
m=5
data = [1,2,3,2,5]

count =0
interval_sum=0
end=0

for start in range(n):
    while interval_sum < m and end<n :
        interval_sum += data[end]
        end += 1
        
        
        
import itertools

monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))

print(result)    



### 소수 찾기(에라토스테네스의 체 방법)

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
            
    return num


a = solution(16)
a

for i in a:
    print(i, end=' ')
    
    
l = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
sum(l)

import numpy
dir(numpy)




a = ['a','b','c','d','1','2','3']
result = ''.join(a)
result


import math
a = math.lcm(2,3)
a


my_string = 'abcdef'
letter = 'f'

answer = ''

for i in range(len(my_string)):
    if my_string[i] != letter:
        answer += my_string[i]
    





import re

target = 'bd'

a = re.compile(target)
b=a.search(my_string)    
b

n=1234
a=set(n)


n = 1234

answer = 0

for i in range(8):
    if n // (10**i) ==0:
        q = i
        break
    
    q

for i in range(q-1,-1,-1):
    answer += n // (10**i)
    n = n%(10**i)
    
    print(answer,n)


b= list(str(n))
b



s = '1 2 3 4'


l = list(map(int, s.split(' ')))

max(l)
min(l)

answer = str(max(l)) + ' ' + str(min(l))


a = "3people unFollowed me"	
a = a.lower()

b=a.lower().split(' ')
b

for i in range(len(b)):
    b[i] = b[i][0].upper() + b[i][1:]

answer = ' '.join(b)




s="1111111"	
n = s.count(str('1'))
zero_count = s.count(str('0'))
count = 1


def recur(n,count, zero_count):
    a=0

    
    if n == 1 :

        return 
        
    while n // 2 >= 1:
        if n % 2 ==1:
            a += 1
            n = n//2

        else:
            zero_count += 1
            n = n//2
            
    
    n = a + 1
    count += 1 
    


    recur(n,count, zero_count)
    

    
        
  
recur(7,1, 0)

count


### for문 돌려


s="1111111"	
n = s.count('1')
zero_count = s.count(str('0'))
count = 1




s="1111111"	
n = s.count(str('1'))
zero_count = s.count(str('0'))
count = 1

cnt, zero_cnt =0,0

while s != '1':
    cnt += 1
    l = s.count('1')
    zero_cnt += s.count('0')
    s = bin(l)[2:]
    
    
l = 7
s = bin(l)[2:]
s


a = []

for i in range(n):
    for j in range(n):
        a.append(j+1)
        
        
        
n=5
l=7
r=14

l_q = l//n
r = r//n - l//n
l_r = l %n
r_r = r%n

arr =[]

for i in range(r+1):
    l_q = l//n +i
    

    if l_q == r//n:
        l_r = r%n
        for j in range(l_r+1):
            if l_q >= j:
                arr.append(l_q+1)
                
            else :
                arr.append(l_r+1)
                
        
    while l_r<5:
        if l_q >= l_r:
            arr.append(l_q+1)
            l_r += 1
        else :
            arr.append(l_r+1)
            l_r += 1
    
    l_r = 0

arr

n=4
left=7
right=14

l_q = left//n
r = right//n - left//n
l_r = left %n
r_r = right%n

arr =[]

for i in range(r+1):

    if l_q == right//n:
        
        l_r = r_r
        
        for j in range(l_r+1):
            if l_q >= j:
                arr.append(l_q+1)

            else :
                arr.append(l_r+1)


    while l_r<n and l_q != right//n:
        print(l_q,l_r)
        if l_q >= l_r:
            arr.append(l_q+1)
            l_r += 1
        else :
            arr.append(l_r+1)
            l_r += 1

    l_r = 0
    l_q += 1

arr





































