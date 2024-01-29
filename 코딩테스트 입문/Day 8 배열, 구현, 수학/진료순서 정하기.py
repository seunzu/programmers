# def solution(emergency):
#     sorted_emergency = sorted(emergency, reverse=True)
#     answer = []
#     for i in emergency:
#         index = sorted_emergency.index(i) + 1
#         answer.append(index)
#     return answer

def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

n = list(map(int, input().split()))
print(solution(n))