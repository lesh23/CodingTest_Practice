### 문제1
# 접근 방법 : 리스트에서 두 수를 바꿔서 만들 수 있는 전체 리스트를 구하고 -> 그 리스트에서 나눠서 합을 구해서 같으면 answer +1
a = [1,2,1,2]
a = [-1,-2,2,1]
a = [4,2,4,-3,-1]

a=[4,3,-2,-1]
from itertools import combinations

# index로 이루어진 리스트 만들어서, 길이가 n인 list에서 두 개의 숫자를 골라 배열을 바꾸는 경우의 수(nC2) 구하기
l = [i for i in range(len(a))]
answer = 0

for i,j in list(combinations(l,2)) :
    b = a[:]
    # 각 index에 해당하는 값이 같으면 값 바꾸지 않고 pass
    if b[i] == b[j]:
        pass
    else :
        # 값이 서로 다르면 값 바꾸기
        b[i],b[j] = b[j], b[i]
        # 값 바꾼후 리스트에서 리스트 분할한 후 합 같은지 확인
        for k in range(1,len(b)):
            if sum(b[:k]) == sum(b[k:]):
                answer += 1
                #print(i,j,b,b[:k],b[k:])
        
# 원래 리스트 a에서 리스트 분할한 후 합 계산 결과 따로 구함        
for k in range(1,len(a)):
    if sum(a[:k]) == sum(a[k:]):
        answer += 1
        #print(a, a[:k],a[k:])

print(answer)



### 문제2
l = ["2022.01.03 6000", "2022.01.05 5000", "2022.01.07 10000", "2022.01.20 50000",
     "2022.01.22 7000", "2022.02.01 15000", "2022.02.03 6000", "2022.02.05 5000", 
     "2022.02.20 50000", "2022.03.01 15000", "2022.03.05 5000", "2022.03.08 10000",
     "2022.03.20 45000", "2022.04.01 15000", "2022.04.03 6000", "2022.04.05 5000",
     "2022.04.10 10500"]
k = 3

# .제거하고 split
for i in range(len(l)):
    l[i] = l[i].replace('.','').split(' ')

# 달별 지출 내역 dict에 저장
a = {}
for x,y in l :
    a[x[:6]] = []

# 교집합 이용할꺼라서 tuple 타입으로 저장
for x,y in l:    
    a[x[:6]].append((int(x[-2:]), int(y)))

a
#{'202201': [(3, 6000), (5, 5000), (7, 10000), (20, 50000), (22, 7000)],
# '202202': [(1, 15000), (3, 6000), (5, 5000), (20, 50000)],
# '202203': [(1, 15000), (5, 5000), (8, 10000), (20, 45000)],
# '202204': [(1, 15000), (3, 6000), (5, 5000), (10, 10500)]}

# 기준이 되는 마지막 달 무조건 포함
answer = a[list(a.keys())[-1]]

for i in list(a.keys())[-k:-1]:
    answer = list(set(answer) & set(a[i]))
    
# tuple을 list로 바꾸고 정렬
answer = sorted([[x,y] for x,y in answer], key = lambda x : x[0])
print(answer)



### 문제3
''' 카드 포인트 문제 '''
members = [['a','-'],['b','a'],['c','b'],['d','b'],['e','-'],['f','d'], ['g','f']]
p = 100

# members를 dic으로 만들기 + answer을 일단 dic으로 만듬
m = {}
answer = {}

for i in members:
    m[i[0]] = i[1]
    answer[i[0]] = 0

# {'a': '-', 'b': 'a', 'c': 'b', 'd': 'b', 'e': '-', 'f': 'd'}
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}

for i in m.keys():
    cnt = 0
    key = i
    while m[key] != '-' :
        answer[m[key]] += int(p * (0.1**cnt))
        key = m[key]
        cnt += 1

l = sorted([[a,b] for a,b in zip(answer.keys(), answer.values())], key=lambda x: x[1],reverse = True)



### 문제4
lotto = [[0,1],[1, 0], [1, 0], [1, 1], [1, 1], [2, 1],[2,0], [3, 0], [3, 0], [4, 0], [5,1],[7,0],[7,0],[7,1],[100, 1]]

d = {}
answer = []

# dict으로 만들기 -> 먼저 list만들기
for i in set([x for x,y in lotto]) :
    d[i] = []
    
# 사람별 로또 당첨여부 dict으로 추가    
for x,y in lotto:
    d[x].append(y)

# {0: [1],
#  1: [0, 0, 1, 1],
#  2: [1, 0],
#  3: [0, 0],
#  4: [0],
#  5: [1],
#  100: [1],
#  7: [0, 0, 1]}

# d에서 당첨여부 판별
for i in d.keys():
    if 1 in d[i]:
        answer.append(d[i].index(1)+1)
    else:
        answer.append(0)

#[1, 3, 1, 0, 0, 1, 1, 3]

print('평균 당첨 횟수 : ', int(sum(answer)/len(answer)))



### 문제5
l = [["sg","sh","hj","Judy","Lucy"],[[3,-1],[2,1],[1,5],[1,3],[2,2]],[3.67,4.16,4.2,3.4,3.2]]

a = []
answer = []

for i in l[0]:
    a.append([i,int(l[2][l[0].index(i)]) , l[1][l[0].index(i)][0]**2 + l[1][l[0].index(i)][1]**2])

# [이름, 학점, 거리]
# a = [['sg', 3, 10], ['sh', 4, 5], ['hj', 4, 26], ['Judy', 3, 10], ['Lucy', 3, 8]]

a = sorted(a, key = lambda x : (-x[1], -x[2], x[0]))

for i in l[0]:
    for x,y in enumerate(a):
        if i == y[0] :
            answer.append(x+1)

print(answer)



### 문제6
k= 6 
arr=[[1,2],[2,3],[4,5]]

k= 8
arr=[[1,2],[1,3],[1,4],[3,4],[5,6]]


# 서로 연결되어 있는 섬들 찾기
land = [arr[0]]
for i in arr:
    for j in land:
        if list(set(i) & set(j)) != []:
            land.remove(j)
            land.append(list(set(i) | set(j)))
        else:
            land.append(i)

land
# [[1, 2, 3], [4, 5]]

# 혼자 있는 섬 개수 찾기
i = [i for i in range(1,k+1)]
for j in land:
    i = list(set(i) - set(j))

i # [6]     

answer = len(land)-1 + len(i)
print(answer)



### 문제 8
l = ['abc de bd','abd ds bhe','abd d bb', 'zye lc']
result = []

for i in range(len(l)) :
    l[i] = l[i].split()

for i in l:
    answer = ''
    for j in range(len(i)):
        if i[j] != '':
            answer += i[j][0]
            i[j] = i[j][1:]

    if answer not in result :
        result.append(answer)
    else :
        while answer in result:
            for j in range(len(i)):
                if i[j] != '' :
                    answer += i[j][0]
                    i[j] = i[j][1:]

                if answer not in result:
                    break
        result.append(answer)

print(result)
