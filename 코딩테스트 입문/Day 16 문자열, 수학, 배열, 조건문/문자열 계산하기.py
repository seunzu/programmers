def solution(my_string):
    return eval(my_string)

# def solution(my_string):
#     s = my_string.split()
#     answer = int(s[0])
#     for i in range(1, len(s), 2):
#         if s[i] == '+':
#             answer += int(s[i+1])
#         else:
#             answer -= int(s[i+1])
#     return answer

s = input()
print(solution(s))