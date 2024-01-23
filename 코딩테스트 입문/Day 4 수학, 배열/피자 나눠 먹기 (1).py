import math

a = int(input())

# def solution(n):
#     if n % 7 == 0:
#         answer = n // 7
#     else:
#         answer = n // 7 + 1
#     return answer

def solution(n):
    return math.ceil(n/7)


print(solution(a))