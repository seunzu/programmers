def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

s, n = input().split()
n = int(n)
print(solution(s, n))