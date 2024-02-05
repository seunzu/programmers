# def solution(quiz):
#     answer = []
#     for s in quiz:
#         if eval(s.split('=')[0]) == int(s.split('=')[1]):
#             answer.append('O')
#         else:
#             answer.append('X')
#     return answer

def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]

# s = input().split(',')
# print(solution(s))
