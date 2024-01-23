str1, str2 = input().split()

def solution(a, b):
    a, b = str(a), str(b)
    if (int(a + b) >= int(2*int(a)*int(b))):
        return int(a + b)
    else:
        return int(2*int(a)*int(b))

print(solution(str1, str2))