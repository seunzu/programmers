def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = [numbers[-1]] + numbers[:-1]
    elif direction == 'left':
        answer = numbers[1:] + [numbers[0]]
    return answer

a = list(map(int, input().split()))
b = input()

print(solution(a, b))
