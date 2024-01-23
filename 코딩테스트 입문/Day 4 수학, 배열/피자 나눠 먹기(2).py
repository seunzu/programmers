import math

a = int(input())

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6

print(solution(a))