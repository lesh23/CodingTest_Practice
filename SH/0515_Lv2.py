# 다음 큰 숫자
def solution(n):
    a = bin(n)[2:]
    c = a.count('1')
    
    while True:
        n = n+1
        b = bin(n)[2:].count('1')
        
        if b==c :
            return n
            break

# 피보나치 수
# for문 + 메모리제이션
def solution(n):
    d = [0]*100001
    d[1],d[2] = 1,1
    for i in range(2,n+1) :
        d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567

# 피보나치 코드 재귀함수 - 런타임에러+시간초과
def fibo(n):
    if n==1 or n==2 :
        return 1
    return fibo(n-1) + fibo(n-2)

def solution(n):
    return fibo(n) % 1234567

# 재귀함수 + 메모리제이션 - 런타임에러
def fibo(n):
    d=[0]*100001
    if n==1 or n==2 :
        return 1
    if d[n] != 0:
        return d[n] 
    
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n] 

def solution(n):
    return fibo(n) % 1234567


# 짝지어 제거하기
# 정확성: 30.3 / 효율성: 0.0 / 합계: 30.3 / 100.0
def solution(s):
    s= list(s)
    answer = 1
    
    if len(s) % 2 ==  1:
        answer = 0

    else :
        while answer == 1 and len(s) > 0 :
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    answer = 1
                    break
                else:
                    answer = 0
    return answer


# 정확성: 40.3 / 효율성: 19.9 / 합계: 60.2 / 100.0 -> 시간 초과
def solution(s):
    s= list(s)
    answer = 1
    d=[0] * 26
    
    if len(s) % 2 ==  1:
        return 0

    for i in range(97,123):
        d[i-97] = s.count(chr(i))
        if d[i-97] % 2 == 1:
            return 0
        
    while answer == 1 and len(s) > 0 :
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                answer = 1
                break
            else:
                answer = 0 
    return answer



