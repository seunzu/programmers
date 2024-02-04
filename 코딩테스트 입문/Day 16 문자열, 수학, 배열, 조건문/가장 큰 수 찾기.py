def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer

a = list(map(int, input().split()))

print(solution(a))