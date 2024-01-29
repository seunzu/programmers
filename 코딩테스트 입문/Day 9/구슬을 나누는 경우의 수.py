import math

def solution(balls, share):
    return math.comb(balls, share)

a, b = input().split()

print(solution(a, b))