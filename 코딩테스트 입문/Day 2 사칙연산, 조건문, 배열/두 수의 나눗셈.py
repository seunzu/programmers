a, b = map(int, input().split())

def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

print(solution(a, b))