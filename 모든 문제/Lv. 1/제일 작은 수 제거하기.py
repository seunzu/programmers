def solution(arr):
    # if len(arr) > 1:
    #     arr.remove(min(arr))
    #     return arr
    # else:
    #     return [-1]
    return [i for i in arr if i > min(arr)]

a = list(map(int, input().split()))

print(solution(a))