def solution(array, height):
    # cnt = 0
    # for i in array:
    #     if i > height:
    #         cnt += 1
    # return cnt

    array.append(height)
    array.sort(reverse=True)
    return array.index(height)


a = list(map(int, input().split()))
b = int(input())

print(solution(a, b))