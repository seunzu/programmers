def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer

a, b = input().split()
a, b = list(a), int(b)

print(solution(a, b))