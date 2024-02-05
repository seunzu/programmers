def solution(array, n):
    # cnt = 0
    # for i in array:
    #     if i == n:
    #         cnt += 1
    # return cnt

    return array.count(n)

a = list(map(int, input().split()))
b = int(input())

print(solution(a, b))