def solution(rsp):
    result = {'2': '0', '0': '5', '5': '2'}
    # answer = ''
    # for i in rsp:
    #     answer += result.get(i)
    # return answer
    return ''.join(result[i] for i in rsp)

n = input()

print(solution(n))