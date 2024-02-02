def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n) # 부피

a = list(map(int, input().split()))
b = int(input())

print(solution(a, b))