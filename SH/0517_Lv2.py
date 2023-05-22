# 영어 끝말잇기

# 카펫
def solution(brown, yellow):
    
    l = sorted([x for x in range(1,brown+yellow+1) if (brown+yellow) % x == 0 ], reverse = True)

    for i in l:
        if yellow % (i-2) == 0:
            return [i,(brown+yellow) // i]

# 구명보트
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
     
    for i in people: 
        if i + people[-1] <= limit :
            people.pop(-1)
            answer += 1
        else :
            answer += 1

    return answer

# 첫번째 코드(정확성 : 75/75, 효율성 :0/25)
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0

    while len(people) != 0:
        if len(people) == 1:
            people.pop(0)
            answer+= 1
            break
        
        if people[0] > limit:
            people.pop(0)
            answer += 1
        else :

            if people[0] + people[-1] <=limit:
                people.pop(-1)
                people.pop(0)
                answer += 1
            else :
                people.pop(0)
                answer += 1

                
    return answer
