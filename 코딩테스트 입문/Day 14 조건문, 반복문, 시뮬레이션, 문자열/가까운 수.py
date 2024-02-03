def solution(array, n):
    array.sort()
    answer = array[0]
    x = abs(n - array[0])

    for i in array:
        if x > abs(n - i):
            x = abs(n - i)
            answer = i

    return answer

# def solution(array, n):
#     array.sort()
#     temp = []
#
#     for i in array:
#         temp.append(abs(n-i))
#
#     return array[temp.index(min(temp))]


a = list(map(int, input().split()))
b = int(input())
print(solution(a, b))