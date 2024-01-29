import math

def solution(balls, share):
    return math.comb(balls, share)

a, b = map(int, input().split())

print(solution(a, b))
