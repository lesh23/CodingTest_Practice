# 두 정수 사이의 합
def solution(a, b):
    p = lambda x,y: sum([i for i in range(x,y+1)]) if x<y else sum([i for i in range(y,x+1)])
    return p(a,b)

# 콜라츠 추측
def solution(num):
    answer = 0
    if num==1: answer = 0
    elif num>1:
        while num!=1:
            answer+=1
            if num%2==0:
                num=num/2
            else:
                num=(num*3)+1
        if answer>=500:
            answer = -1
                
    return answer

# 서울에서 김서방 찾기
def solution(seoul):
    for i,j in enumerate(seoul):
        if j == 'Kim':
            return "김서방은 "+str(i)+"에 있다"