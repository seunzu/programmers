a, b = map(int, input().split())

def solution(slice, n):
    if n % slice == 0:
        answer = n // slice
        return answer
    else:
        answer = n // slice + 1
        answer = n // slice + 1
        return answer

# import math
#
# def solution(slice, n):
#     return math.ceil(n/slice)

print(solution(a, b))