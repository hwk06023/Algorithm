import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

li = [[]]
for _ in range(n):
    li.append(list(map(int, input().split())))

visited = [False] * (n+1)

def bfs(li, node, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        tmp = queue.popleft()
        print(tmp)
        for i in li[tmp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

start = 1
bfs(li, start, visited)