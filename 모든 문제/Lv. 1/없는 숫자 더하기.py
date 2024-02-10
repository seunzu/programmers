def solution(numbers):
    # total = 0
    # for i in range(0, 10):
    #     if i not in numbers:
    #         total += i
    # return total

    return 45 - sum(numbers)

n = list(map(int, input().split()))

print(solution(n))