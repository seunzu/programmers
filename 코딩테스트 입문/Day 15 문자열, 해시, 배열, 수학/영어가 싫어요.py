def solution(numbers):
    nums = ['zero','one','two','three','four','five', 'six','seven','eight','nine']

    for i, n in enumerate(nums):
        numbers = numbers.replace(n, str(i))

    return int(numbers)

s = input()

print(solution(s))