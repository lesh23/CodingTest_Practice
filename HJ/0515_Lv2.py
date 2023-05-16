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

# 짝지어 제거하기