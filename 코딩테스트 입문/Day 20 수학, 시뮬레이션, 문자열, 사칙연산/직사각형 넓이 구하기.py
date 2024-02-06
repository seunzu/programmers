def solution(dots):
    dots.sort(key=lambda x: (x[0], x[1]))
    return abs(dots[0][0] - dots[3][0]) * abs(dots[0][1] - dots[3][1])

# def solution(dots):
#     return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

arr = [list(map(int, input().split())) for _ in range(4)]

print(solution(arr))
