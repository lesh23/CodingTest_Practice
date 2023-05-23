# 영어 끝말잇기
def solution(n, words):
    game=[]
    rnd=0
    person= lambda x: n if (x+1)%n==0 else (x+1)%n
    for i,w in enumerate(words):
        if i%n==0:
            rnd+=1
        if w in game:
            return [person(i), rnd]
        else:
            if game!=[]:
                game.append(w)
                if game[i-1][-1]!=w[0]:
                    return [person(i), rnd]
                else:
                    continue
            else:
                game.append(w)
    return [0,0]


# 카펫


# 구명보트
# 효율성 에러,,;;
def solution(people, limit):
    answer = 0
    ppl = sorted([x for x in people])
    while ppl:
        # print(ppl, ppl[0], ppl[-1])
        if ppl[0] + ppl[-1] <= limit:
            ppl.pop()
            ppl=ppl[1:]
        else:
            ppl.pop()
        answer+=1
    return answer