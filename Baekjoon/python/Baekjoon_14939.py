# 못풀어서 참고함..

import sys

input = sys.stdin.readline

dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]

def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if ny >= 0 and ny < 10 and nx >= 0 and nx < 10:
            b[ny][nx] = (b[ny][nx] + 1) % 2

board = [[0]*10 for _ in range(10)]

for i in range(10):
    line = input()
    for j in range(len(line)):
        if line[j] == "O":
            board[i][j] = 1

first_line_press_case = [101] * (1 << 10)
for case in range(1 << 10):
    tmp_board = [board[i][:] for i in range(10)] 
    cnt = 0

    mask = 1
    for j in range(9, -1, -1):
        if case & mask:
            press(tmp_board, 0, j)
            cnt += 1
        mask <<= 1

    for i in range(1, 10):
        for j in range(10):
            if tmp_board[i - 1][j]: 
                press(tmp_board, i, j)  
                cnt += 1

    if sum(tmp_board[9]) == 0:
        first_line_press_case[case] = cnt

print(min(first_line_press_case))