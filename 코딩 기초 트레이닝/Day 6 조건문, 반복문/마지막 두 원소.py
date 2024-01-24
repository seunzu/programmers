a = list(map(int, input().split()))

def solution(num_list):
    l = len(num_list)
    if num_list[l - 2] < num_list[l - 1]:
        num_list.append(num_list[l - 1] - num_list[l - 2])
    else:
        num_list.append(num_list[l - 1] * 2)
    return num_list

print(solution(a))