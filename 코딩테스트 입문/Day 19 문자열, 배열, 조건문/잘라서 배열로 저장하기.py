def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

s, num = input().split()
num = int(num)

print(solution(s, num))