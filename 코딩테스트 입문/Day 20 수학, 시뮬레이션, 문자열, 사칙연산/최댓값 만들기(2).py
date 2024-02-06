def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

n = list(map(int, input().split()))

print(solution(n))