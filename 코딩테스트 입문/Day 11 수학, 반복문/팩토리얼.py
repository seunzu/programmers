from math import factorial

# def solution(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#         if result == n:
#             return i
#         elif result > n:
#             return i-1
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

num = int(input())

print(solution(num))