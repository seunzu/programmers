# def solution(n):
#     n = list(map(int, str(n)))
#     return sum(n)

def solution(n):
    return sum(int(i) for i in str(n))

num = list(map(int, input()))
print(solution(num))