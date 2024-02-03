# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer += i
#     return answer

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

s = input()

print(solution(s))