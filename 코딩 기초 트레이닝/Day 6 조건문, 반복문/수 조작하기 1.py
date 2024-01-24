a, b = input().split()
a = int(a)


def solution(n, control):
    answer = n

    for k in control:
        if k == "w":
            answer += 1
        elif k == "s":
            answer -= 1
        elif k == "d":
            answer += 10
        elif k == "a":
            answer -= 10

    return answer

print(solution(a, b))