def solution(hp):
    return (hp // 5) + ((hp % 5) // 3) + (((hp % 5) % 3) // 1)

n = int(input())

print(solution(n))