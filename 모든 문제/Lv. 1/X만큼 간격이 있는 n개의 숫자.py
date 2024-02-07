def solution(x, n):
    return [i for i in range(x, x*(n+1), x)]

    # return [i * x for i in range(1, n+1)]

a, b = map(int, input().split())

print(solution(a, b))