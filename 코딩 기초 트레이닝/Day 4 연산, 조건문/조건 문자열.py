a, b, c, d = input().split()

def solution(ineq, eq, n, m):
    if eq == "!" :
        if ineq == "<" :
             return int(n<m)
        else:
            return int(n>m)
    else:
        if ineq == "<" :
             return int(n<=m)
        else:
            return int(n>=m)

print(solution(a, b, c, d))