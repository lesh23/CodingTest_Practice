### 문제1
# 접근 방법 : 리스트에서 두 수를 바꿔서 만들 수 있는 전체 리스트를 구하고 -> 그 리스트에서 나눠서 합을 구해서 같으면 answer +1
a = [1,2,1,2]
a = [-1,-2,2,1]
a = [4,2,4,-3,-1]
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



### 문제2



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



