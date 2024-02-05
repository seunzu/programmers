def solution(my_string):
    return ''.join(sorted(my_string.lower()))

s = input()

print(solution(s))