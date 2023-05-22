# 영어 끝말잇기
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] :
            return [(i%n)+1, (i//n)+1]
        elif words[i] in words[:i]:            # enumerate로 푸는 방법,,
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(0,5000):                     # 범위 이게 최선이야?
        for j in range(0,5000):
            if i+j == (brown-4)/2 and i*j == yellow:
                return [j+2,i+2]

# 구명보트