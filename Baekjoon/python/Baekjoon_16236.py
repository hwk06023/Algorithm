import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = [i, j]
            graph[i][j] = 0

def bfs():
    dx = [-1, 0, 0, 1]  
    dy = [0, -1, 1, 0]
    visited = [[-1] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = 0
    queue = deque()
    queue.append(shark)
    eat = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    if 0 < graph[nx][ny] < shark_size:
                        eat.append([nx, ny, visited[nx][ny]])
    if not eat:
        return None
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0]       

shark_size = 2
shark_eat = 0
time = 0

while True:
    result = bfs()
    if result == None:
        print(time)
        break
    else:
        time += result[2]
        shark = [result[0], result[1]]
        graph[result[0]][result[1]] = 0
        shark_eat += 1
        if shark_eat >= shark_size:
            shark_size += 1
            shark_eat = 0

# 블로그 참고함.