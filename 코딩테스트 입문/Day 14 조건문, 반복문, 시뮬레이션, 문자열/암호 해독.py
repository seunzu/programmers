def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer

a, b = input().split()
b = int(b)

print(solution(a, b))