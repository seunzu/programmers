def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))

a = input()

print(solution(a))