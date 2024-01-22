a = list(map(int, input().split()))

def solution(numbers):
    # answer = []
    #
    # for i in numbers:
    #     answer.append(i*2)
    #
    # return answer

    return [num*2 for num in numbers]

print(solution(a))