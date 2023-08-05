import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())

visit = [0] * (n+1)
graph = []
for _ in range(n+1):
    graph.append([])

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])

#DFS
dfs_li = []
def dfs(graph, i, visit):
    visit[i] = 1
    dfs_li.append(i)
    for x in graph[i]:
        if visit[x] == 0:
            dfs(graph, x, visit)
i=start
dfs(graph, i, visit)
print(" ".join(map(str, dfs_li)))

visit = [0] * (n+1)
#BFS
bfs_li = [start]
visit[start] = 1
i=0
tmp_b = 0
while(1):
    for x in graph[bfs_li[i]]:
        if visit[x] == 0:
            tmp_b += 1
            visit[x] = 1
            bfs_li.append(x)
    if tmp_b == 0:
        break
    i+=1
    tmp_b -= 1

print(" ".join(map(str, bfs_li)))
