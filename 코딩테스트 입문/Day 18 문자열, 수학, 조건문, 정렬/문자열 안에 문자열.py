def solution(str1, str2):
#     for i in range(len(str1)):
#         if str1[i:i+len(str2)] == str2:
#             return 1
#     return 2

    return 1 if str2 in str1 else 2


s1, s2 = input().split()

print(solution(s1, s2))

