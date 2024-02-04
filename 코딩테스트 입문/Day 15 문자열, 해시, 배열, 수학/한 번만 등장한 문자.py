# def solution(s):
#     answer = ''
#     for i in s:
#         if s.count(i) == 1:
#             answer += i
#     return ''.join(sorted(answer))

def solution(s):
    answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
    return answer


a = input()

print(solution(a))