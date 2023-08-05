import sys

input = sys.stdin.readline
n, m = map(int, input().split())

n_li = [0]*(n)
n_li.insert(1, 100)
graph = []
v_li = []
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    v, w = map(int, input().split())
    if v not in v_li:
        v_li.append(v)
    graph[v].append(w)

v_li = sorted(v_li)

for i in v_li:
    for j in range(len(graph[i])):
        n_li[graph[i][j]] += n_li[i] / len(graph[i])
    n_li[i] = 0
    
print(max(n_li))