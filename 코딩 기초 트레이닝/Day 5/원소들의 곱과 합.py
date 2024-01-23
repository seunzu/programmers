nList = list(map(int, input().split()))

def solution(num_list):
    a = 1
    sum = 0

    for i in num_list:
        a *= i
        sum += i

    sum2 = sum ** 2

    if a < sum2:
        return 1
    else:
        return 0


print(solution(nList))