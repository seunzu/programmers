arrayList = list(input().split())

def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer

print(solution(arrayList))