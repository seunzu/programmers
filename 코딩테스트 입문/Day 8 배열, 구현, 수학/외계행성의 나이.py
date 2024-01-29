# def solution(age):
#     answer = ''
#     for i in str(age):
#         answer += chr(int(i) + 97)
#     return answer

def solution(age):
    return ''.join([chr(int(i) + 97) for i in str(age)])

# def solution(age):
#     return str(age).translate(str.maketrans('0123456789', 'abcdefghij'))

n = int(input())

print(solution(n))