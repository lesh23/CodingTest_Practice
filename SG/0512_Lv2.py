# 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack ==[]:              # ")" 넣기 전 이미 비어있으면 F
                return False
            else:
                stack.pop()             # "(" 들어가 있으면 빼기
    if stack != []:                     # 다 했는데 남아있는게 있으면 F
        return False
    return True

# 이진 변환 만들기
def solution(s):
    answer = []
    cnt=0
    zero=0
    while 1:
        if s == "1":
            break
        cnt += 1
        zero += s.count("0")
        s = s.replace("0", "")
        new = len(s)
        s = bin(new)[2:]
    answer.append(cnt)
    answer.append(zero)
    return answer

# 숫자의 표현
def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            if (j-i+1)*(i+j)/2 ==n:
                answer += 1
    return answer                   # 효율성 0점짜리 풀이 ㅠ^ㅠ 아닐 때 다시 생각해서 풀기  
