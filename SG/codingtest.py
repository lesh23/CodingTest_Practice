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


#  배열 나누기 
def sol2(arr):
    cnt = 0

    for k in range(len(arr)):
        if sum(arr[k:]) == sum(arr[:k]):
            if arr[k:]!=[] and arr[:k]!=[]:
                print(arr[k:],arr[:k])
                cnt += 1


    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                for k in range(len(arr)):
                    if sum(arr[k:]) == sum(arr[:k]):
                        if arr[k:]!=[] and arr[:k]!=[]:
                            print(arr[k:],arr[:k])
                            cnt += 1
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


# 포인트 
def solution(p,arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i][0]== arr[j][1]:
                arr[j]= [arr[j][0]]+arr[i]
#[['a', '-'],['b', 'a', '-'],['c', 'b', 'a', '-'],['d', 'b', 'a', '-'],['e', '-'],['f', 'd', 'b', 'a', '-']]

    answer = []
    for k in range(0,len(arr)):
        for m,n in enumerate(arr[k]):
            answer.append([n,m])


    rem = [item for item in answer if item[0]!='-']
#[['a', 0], ['b', 0], ['a', 1], ['c', 0], ['b', 1], ['a', 2], ['d', 0], ['b', 1], ['a', 2], ['e', 0], ['f', 0], ['d', 1], ['b', 2], ['a', 3]]

    result = []
    for item in rem:
        key, value = item
        for point in result:
            if point[0] == key:
                point[1] += int(p * ((0.1) ** (value-1)))
                break
        else:
            result.append([key, 0])

    return sorted(result , key = lambda x:x[1],reverse = True)


# 기숙사 배정 
def solution(arr):
    answer = []
    result = []
    for i in range(len(arr[0])):
        answer.append([arr[0][i],(arr[1][i][0]**2)+(arr[1][i][1]**2),int(arr[2][i])])       #리스트 합치기
        
    names = [i[0] for i in sorted(answer,key = lambda x:(-x[2],-x[1],x[0]))]                #정렬하고 이름만 나열
    
    for name in arr[0]:
        result.append(names.index(name)+1)      # 인덱스 출력
        
    return result


# 로또 
def sol1(lottery):
    dic = {}
    answer = []
    
    for key, value in lottery:
        if key not in dic:
            dic[key] = []
        dic[key].append(value) # 당첨 여부 리스트로 만들기
       
    for k in dic.values():
        if 1 in k:
            answer.append(k.index(1)+1)
        else:
            answer.append(0)
    
    return int(sum(answer)/3)


# 다리 건설