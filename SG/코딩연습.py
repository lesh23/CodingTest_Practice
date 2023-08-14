

 

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