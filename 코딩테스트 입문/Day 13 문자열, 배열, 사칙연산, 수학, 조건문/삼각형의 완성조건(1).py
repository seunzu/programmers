# def solution(sides):
#     sides = sorted(sides, reverse=True)
#     if sides[0] < sides[1] + sides[2]:
#         return 1
#     else:
#         return 2

def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2

l = list(map(int, input().split()))
print(solution(l))