def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n = n // i
        else:
            i += 1
    return sorted(list(set(answer)))

# def solution(n):
#     answer = []
#     for i in range(2, n+1):
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#         if n % i == 0 and count < 3:
#             answer.append(i)
#     return answer

a = int(input())

print(solution(a))