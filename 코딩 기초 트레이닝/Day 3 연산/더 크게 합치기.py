str1, str2 = input().split()

def solution(a, b):
    a, b = str(a), str(b)
    if (int(a + b) >= int(b + a)):
        return int(a + b)
    else:
        return int(b + a)

print(solution(str1, str2))