def solution(n):
    # for i in range(1, n):
    #     if i*i == n:
    #         return 1
    # return 2

    return 1 if (n ** 0.5).is_integer() else 2

num = int(input())

print(solution(num))