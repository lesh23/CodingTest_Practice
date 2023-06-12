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
        for point in result:
            if point[0] == key:
                point[1] += 100.0 * (0.1) ** (value-1)
                break
        else:
            result.append([key, 0])
    return result

# 리스트 컴프리헨션 [표현식 for 항목 in 시퀀스]
numbers = [x for x in range(10)]
print(numbers)