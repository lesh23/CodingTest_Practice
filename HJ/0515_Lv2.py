# 다음 큰 숫자
def solution(n):
    # 1의 개수 구하기
    ones= len([x for x in bin(n)[2:] if x == '1'])
    # answer = 0

    # n++ 반복. 1의 개수가 맞을 때 까지 (효율 똥일듯)
    while True:
        n+=1
        tmp = len([y for y in bin(n)[2:] if y=='1'])
        if ones == tmp:
            return n
        else:
            continue
        

# 피보나치 수
def solution(n):
    num = fib(n)
    if num!=0:
        answer = num%1234567
    return answer

def fib(x):
    if x<2: return x
    elif x<0: return 0
    else:
        return (fib(x-1)+(fib(x-2)))
    
# def solution(n):
#     for i in reversed(range(n+1)):
#         print(i)

# 짝지어 제거하기
def solution(s):
    tmp=[]
    
    for i in s: 
        if len(tmp)==0:
            tmp.append(i)
        else:
            if i == tmp[-1]:
                tmp.pop()
            else:
                tmp.append(i)
                
    if len(tmp)==0: return 1
    else: return 0