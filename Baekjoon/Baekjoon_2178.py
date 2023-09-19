import sys

input = sys.stdin.readline

n, m  = map(int, input().split())

li = []
for i in range(n):
    li.append(input())

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

queue = [[0, 0]]

while queue:
    x, y = queue.pop(0)
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in range(4):
        dx = x + [0, 0, -1, 1][i]
        dy = y + [-1, 1, 0, 0][i]
        if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and li[dx][dy] == '1':
            visited[dx][dy] = visited[x][y] + 1
            queue.append([dx, dy])
