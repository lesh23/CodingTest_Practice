''' Chap 3. 내장자료구조, 함수, 파일 '''

### 튜플 : *rest -> rest가 자료 이름
tu = 1,2,4,5,8
a,b,*c = tu
# a =1, b=2, c=[4,5,8]

### 리스트
li = [1,2,3,4]
li.insert(0, -1) # 0번 인덱스에 값 -1 추가
li # [-1, 1, 2, 3, 4]

li.pop(0) # 0번 인덱스의 값 삭제 [1,2,3,4]
li.remove(3) # 값 제거, 중복 값 있을시 맨 앞에 위치한 값 삭제 [1,2,4] 
li.extend(['a','b']) # 리스트 이어붙이기, + 연산자로도 가능
li # [1, 2, 4, 'a', 'b']

# 리스트 정렬
a = [2,61,84,1,5,3,6,544]
a.sort() # 새로운 리스트 생성없이 그대로 리스트 정렬

b = ['a', 'apple', 'banana', 'cat', 'watermelon']
b.sort(key = len) # 리스트를 문자열의 길이 순으로 정렬 가능
b # ['a', 'cat', 'apple', 'banana', 'watermelon']


### bisect : 정렬된 배열에서 이진탐색
# import bisect
a = [1,2,2,3,4,5,8]





''' Chap 4. Numpy 기본 '''
import numpy as np

l = [1,2,3,4,5,6]
a = np.array(l)
a = np.arange(15)
a
a.dtype
b = a.astype(np.float32)
b

# 논리 연산자
# &(and), |(or)

# 팬시 색인
arr = np.empty((8,4))

for i in range(8):
    arr[i] = i

arr[[4,3,0,6]]
# array([[4., 4., 4., 4.],
#        [3., 3., 3., 3.],
#        [0., 0., 0., 0.],
#        [6., 6., 6., 6.]])

# 유니버셜함수
arr1 = np.random.rand(8)
arr2 = np.random.rand(8)

np.sqrt(arr2) # 제곱근
np.exp(arr2) # e
np.maxinum(arr1, arr2) # arr1, arr2 중 가장 큰 값 반환 / fmax : NAN값 무

arr = np.random.randn(7) *5
remainder, whole_part = np.modf(arr) # 정수부분과 소수부분 반환

# 배열 연산으로 조건절 표현하기(163p)
xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.arraY([5,4,3,2,1])
cond = np.array([True, False, False, True, True])

# result1과 result가 같음
result1 = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]
result2 = np.where(cond, xarr, yarr)
# np.where의 경우 두번째, 세 번재 인자는 배열이 아니어도 됨

# p169. 집합 관련 함수
arr = np.array([1,1,2,6,2,4,8,6,1,4,5])
np.unique(arr)
sorted(set(arr))





''' Chap 5. pandas 시작하기 '''
import pandas as pd

# 184p
sdata = {'Ohio' : 35000, 'Texas':71000, 'Oregon':16000,'Utah' : 5000}
obj3 = pd.Series(sdata)
obj3
states = ['California', 'Ohio','Oregon','Texas']
obj4 = pd.Series(sdata, index = states)
obj4

# 193p
pop = {'Nevada' : {2001 : 2.4, 2002:2.9},
       'Ohio' : {2000:1.5, 2001:1.7, 2002:3.6}}

frame3 = pd.DataFrame(pop)
frame3

frame3.T
pd.DataFrame(pop, index = [2001,2002,2003])






















