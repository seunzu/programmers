import statistics

def solution(arr):
    return statistics.mean(arr)

a = list(map(int, input().split()))

print(solution(a))