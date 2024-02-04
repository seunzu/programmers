# def solution(s1, s2):
#     cnt = 0
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 cnt += 1
#
#     return cnt

def solution(s1, s2):
    return len(set(s1)&set(s2))


a = list(input().split())
b = list(input().split())

print(solution(a, b))