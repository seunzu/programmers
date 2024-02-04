def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)

s = list(input())
a, b = map(int, input().split())

print(solution(s, a, b))