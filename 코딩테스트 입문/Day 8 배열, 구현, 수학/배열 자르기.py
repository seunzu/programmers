def solution(numbers, num1, num2):
    numbers = list(numbers)
    num1, num2 = int(num1), int(num2)
    return numbers[num1:num2+1]

a, b, c = input().split()
print(solution(a, b, c))