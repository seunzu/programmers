def solution(n, t):
    # return n*(2**t)
    return n << t

a, b = map(int, input().split())

print(solution(a, b))