def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    answer = my_string
    for i in aeiou:
        answer = answer.replace(i, '')
    return answer

s = input()

print(solution(s))