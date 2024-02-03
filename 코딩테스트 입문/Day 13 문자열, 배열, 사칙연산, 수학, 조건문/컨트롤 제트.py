# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         if s[i] == "Z":
#             answer -= int(s[i-1])
#         else:
#             answer += int(s[i])
#     return answer

def solution(s):
    stack = []
    for i in s:
        if i != 'Z':
            stack.append(int(i))
        else:
            if stack:
                stack.pop()

    return sum(stack)

l = input().split()

print(solution(l))