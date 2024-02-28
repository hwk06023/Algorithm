import sys

input = sys.stdin.readline

n = int(input())
li = [[]]
for _ in range(n):
    li.append(list(map(int, input().split())))

visited = [False] * (n+1)

def dfs(li, node, visited):
    visited[node] = True
    print(node)
    for x in li[node]:
        if not visited[x]:
            dfs(li, x, visited)
start = 1
dfs(li, start, visited)