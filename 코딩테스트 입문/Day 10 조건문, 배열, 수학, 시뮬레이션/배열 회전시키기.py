# def solution(numbers, direction):
#     answer = []
#     if direction == 'right':
#         answer = [numbers[-1]] + numbers[:-1]
#     elif direction == 'left':
#         answer = numbers[1:] + [numbers[0]]
#     return answer

from collections import deque

def solution(numbers, direction):
    numbers_deque = deque(numbers)

    if direction == 'right':
        numbers_deque.rotate(1)
    elif direction == 'left':
        numbers_deque.rotate(-1)
    return list(numbers_deque)

a = list(map(int, input().split()))
b = input()

print(solution(a, b))
