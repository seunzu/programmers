def solution(keyinput, board):
    x, y = 0, 0
    move = {'left' : (-1, 0), 'right' : (1, 0), 'up' : (0, 1), 'down' : (0, -1)}
    x_lim, y_lim = board[0] // 2, board[1] // 2
    for k in keyinput:
        dx, dy = move[k]
        if abs(x + dx) > x_lim or abs(y + dy) > y_lim:
            continue
        else:
            x, y = x + dx, y + dy

    return [x, y]

lr = list(input().split())
b = list(map(int, input().split()))

print(solution(lr, b))
