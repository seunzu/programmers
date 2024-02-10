def solution(arr):
    arr.sort(reverse=True)
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
        return arr
    else:
        return arr

a = list(map(int, input().split()))

print(solution(a))