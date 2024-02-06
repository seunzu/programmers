def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x, n = 0, 0

    for i in polynomial:
        if i.isdigit():
            n += int(i)
        else:
            if i == 'x':
                x += 1
            else:
                x += int(i[:-1])

    if x == 0:
        return str(n)
    elif x == 1:
        return 'x + ' + str(n) if n != 0 else 'x'
    else:
        return f'{x}x + {n}' if n != 0 else f'{x}x'

s = input()

print(solution(s))