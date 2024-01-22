import numpy as np

a = list(map(int, input().split()))

def solution(array):
    answer = int(np.median(array))
    return answer


print(solution(a))