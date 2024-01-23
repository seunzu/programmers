import statistics

a = list(map(int, input().split()))

def solution(array):
    answer = statistics.mode(array)
    return answer


print(solution(a))