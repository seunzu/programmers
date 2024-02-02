# def solution(my_string):
#     answer = 0
#     for s in my_string:
#         if s.isdigit():
#             answer += int(s)
#     return answer

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())


s = input()
print(solution(s))