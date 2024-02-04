# def solution(num, k):
#     for i, c in enumerate(str(num)):
#         if int(c) == k:
#             return i+1
#     return -1

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

a, b = map(int, input().split())

print(solution(a, b))