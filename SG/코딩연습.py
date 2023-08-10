# 포인트 
def point(m,arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i][0]== arr[j][1]:
                arr[j]= [arr[j][0]]+arr[i]
    answer = []
    for k in range(0,len(arr)):
        for m,n in enumerate(arr[k]):
            answer.append([n,m])
#[['a', '-'],['b', 'a', '-'],['c', 'b', 'a', '-'],['d', 'b', 'a', '-'],['e', '-'],['f', 'd', 'b', 'a', '-']]
    rem = [item for item in answer if item[0]!='-']
    result = []

    for item in rem:
        key, value = item
        for p in result:
            if p[0] == key:
                p[1] += m * (0.1) ** (value-1)
                break
        else:
            result.append([key, 0])
    return sorted(result , key = lambda item:item[1])


#[['a', '-'],['b', 'a', '-'],['c', 'b', 'a', '-'],['d', 'b', 'a', '-'],['e', '-'],['f', 'd', 'b', 'a', '-']]
 

# 리스트 컴프리헨션 [표현식 for 항목 in 시퀀스]
numbers = [x for x in range(10)]
print(numbers)


# 딕셔너리
def solution(n):
    answer = {}
    for i in n:
        answer[i] = n.count(i)
    return answer
solution([1,2,2,3,2,4,2,4,1,2,2,3,4])
{1: 2, 2: 6, 3: 2, 4: 3}


# 딕셔너리 key 값 정렬 def solution(n):
def solution(n):
    answer = {}
    for i in n:
        answer[i] = n.count(i)
    return sorted(answer.items(), key= lambda item:item[0])
solution([1,2,2,3,2,4,2,4,1,2,2,3,4])
[(1, 2), (2, 6), (3, 2), (4, 3)]


# 딕셔너리 value 값 정렬 def solution(n):
def solution(n):
    answer = {}
    for i in n:
        answer[i] = n.count(i)
    return sorted(answer.items(), key= lambda x:x[1])
solution([1,2,2,3,2,4,2,4,1,2,2,3,4])
[(1, 2), (3, 2), (4, 3), (2, 6)]


# zip 사용해서 딕셔너리 만들기
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(dict(zip(genres,plays)))
# 결과 {'classic': 800, 'pop': 2500} => 값의 합이 나옴


# 순열
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))


# 조합
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))