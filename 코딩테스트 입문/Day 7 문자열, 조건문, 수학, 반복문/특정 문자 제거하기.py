# def solution(my_string, letter):
#     answer = ''
#
#     for i in my_string:
#         if i != letter:
#             answer += i
#
#     return answer

def solution(my_string, letter):
    return my_string.replace(letter, '')

s1, s2 = input().split()

print(solution(s1, s2))