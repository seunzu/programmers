import numpy as np

a = list(map(int, input().split()))

def solution(array):
    answer = np.median(array)
    return answer


print(solution(a))