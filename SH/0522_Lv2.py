# H-Index

# 연속 부분 수열 합의 개수
def solution(elements):
    # elements 길이 2배로 늘려줌
    elements = elements*2
    l = []
    
    # 그리고 수열합 실행
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            l.append(sum(elements[j:j+i+1]))

    # set으로 중복제거                
    return len(set(l))

# 시간 초과
def solution(elements):
    l = []

    for i in range(len(elements)):
        for j in range(len(elements)):
            l.append(sum(elements[(j+x)%len(elements)] for x in range(i+1)))
            
    return len(set(l))
        
        
# 시간 초과
# 중간까지 계산하고 뒤에 값은 앞의 계산값을 빼준 값임을 이용
def solution(elements):
    l= set(elements)
    
    for i in range(1, len(elements)//2+1):
        for j in range(len(elements)):
            l.add(sum(elements[(j+x)%len(elements)] for x in range(i+1)))
            
    for i in list(l):
        l.add(sum(elements) - i)
    
    l.add(sum(elements))
    
    return len(l)

# [1차] 캐시