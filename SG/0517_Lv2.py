# 영어 끝말잇기

# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(0,5000):                     # 범위 이게 최선이야?
        for j in range(0,5000):
            if i+j == (brown-4)/2 and i*j == yellow:
                return [j+2,i+2]

# 구명보트