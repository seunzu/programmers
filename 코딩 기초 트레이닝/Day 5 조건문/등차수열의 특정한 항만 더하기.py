bool = []
n, m, bool = input().split()
n, m = int(n), int(m)

# a + d(n-1)
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

print(solution(n, m, bool))