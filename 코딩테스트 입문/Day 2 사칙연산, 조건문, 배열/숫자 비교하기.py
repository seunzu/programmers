a, b = map(int, input().split())

def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1


print(solution(a, b))