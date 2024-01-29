# def solution(n):
#     sum = 0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             sum += i
#     return sum

def solution(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum

a = int(input())

print(solution(a))