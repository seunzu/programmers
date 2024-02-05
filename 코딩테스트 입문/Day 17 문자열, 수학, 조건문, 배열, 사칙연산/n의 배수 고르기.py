
# def solution(n, numlist):
#     answer = []
#     for i in numlist:
#         if i % n == 0:
#             answer.append(i)
#     return answer

def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

a = int(input())
b = list(map(int, input().split()))

print(solution(a, b))