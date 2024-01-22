import math

a, b, c, d = map(int, input().split())

def solution(numer1, denom1, numer2, denom2): # 분자 numer, 분모 denom
    numer = denom1 * numer2 + denom2 * numer1
    denom = denom1 * denom2
    gcd = math.gcd(denom, numer)
    return [numer // gcd, denom // gcd]

print(solution(a, b, c, d))