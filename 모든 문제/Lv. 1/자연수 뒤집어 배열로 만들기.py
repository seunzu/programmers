def solution(n):
    return list(map(int, reversed(str(n))))

num = int(input())

print(solution(num))