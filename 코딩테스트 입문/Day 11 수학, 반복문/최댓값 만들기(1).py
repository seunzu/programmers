def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

n = list(map(int, input().split()))

print(solution(n))