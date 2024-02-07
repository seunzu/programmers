def solution(a, b):
	return sum(range(min(a, b), max(a, b) + 1))

n1, n2 = map(int, input().split())

print(solution(n1, n2))

