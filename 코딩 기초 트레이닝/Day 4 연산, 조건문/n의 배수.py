a, b = map(int, input().split())

def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0

print(solution(a, b))