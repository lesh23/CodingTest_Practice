# 포인트 
def point(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i][0]== arr[j][1]:
                arr[j]= [arr[j][0]]+arr[i]
    answer = []
    for k in range(0,len(arr)):
        for m,n in enumerate(arr[k]):
            answer.append([n,m])

    rem = [item for item in answer if item[0]!='-']
    result = []

    for item in rem:
        key, value = item
        for p in result:
            if p[0] == key:
                p[1] += 100.0 * (0.1) ** (value-1)
                break
        else:
            result.append([key, 0])
    return result

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
    return sorted(answer.items(), key= lambda item:item[1])
solution([1,2,2,3,2,4,2,4,1,2,2,3,4])
[(1, 2), (3, 2), (4, 3), (2, 6)]