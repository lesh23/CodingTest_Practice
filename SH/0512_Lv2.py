# 올바른 괄호
def solution(s):
    s = list(s)
    l=0 # 괄호 짝꿍 찾는 변수
    l_c, r_c=0,0 # 각 괄호 개수
    re = []
    
    for i in range(len(s)):
        # (괄호는 +1 , )괄호는 -1로 계산

        if s[i] == '(':
            l += 1
            l_c += 1
            re.append(l)              
        else :
            l -= 1
            r_c +=1
            re.append(l)  

    # 시작이 ) 이거나, 괄호 총 개수가 홀수거나, )괄호 개수가 (괄호보다 많거나, 괄호 짝꿍이 안맞거나
    if re[0] < 0 or len(s)%2==1 or re.count(-1)>0 or l_c != r_c:
        return False
    else:
        return True


# 이진 변환 만들기
def solution(s):
    cnt, zero_cnt =0,0

    while s != '1':
        cnt += 1
        l = s.count('1')
        zero_cnt += s.count('0')
        s = bin(l)[2:]
        
    return [cnt, zero_cnt]


# 숫자의 표현
def solution(n):
    answer = 0
    # 연속하는 수 방정식 계산하는 방법으로 생각
    # x+(x+1)+(x+2) = 15 를 예로 들면 3x + (1+2) = 15가 됨
    # 3x = 15 - (1+2)가 됨으로 for문을 이용해서 ix + (i-1)i/2 = n 이라는 방정식을 해결한다고 생각하고 접근
    for i in range(1,n+1):
        if n-(i-1)*i/2 > 0 :
            if (n-(i-1)*i/2) % i == 0:
                answer += 1
        else :
            break
        
    return answer