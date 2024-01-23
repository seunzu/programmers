n, m, f = input().split()

def solution(a, b, flag):
    return a+b if flag else a-b

print(solution(n, m, f))