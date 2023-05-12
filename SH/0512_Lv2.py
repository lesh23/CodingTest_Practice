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