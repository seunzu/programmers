def solution(n):
    # return min([i for i in range(1, n+1) if n % i == 1])
    return [i for i in range(1, n+1) if n % i == 1][0]

num = int(input())

print(solution(num))