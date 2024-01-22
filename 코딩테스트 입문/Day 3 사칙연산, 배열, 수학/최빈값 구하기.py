from scipy import stats

a = list(map(int, input().split()))

def solution(array):
    answer = stats.mode(array)[0]
    return int(answer)


print(solution(a))