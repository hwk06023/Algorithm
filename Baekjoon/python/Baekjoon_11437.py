import sys
input = sys.stdin.readline

n = int(input())
parents = [0] * (n + 1)
depth = [0] * (n + 1)
cases = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    parents[b] = a

for i in range(1, n + 1):
    if parents[i] == 0:
        root = i
        break

def dfs(x, d):
    depth[x] = d
    for i in cases[x]:
        if depth[i] == 0:
            dfs(i, d + 1)

for i in range(1, n + 1):
    if parents[i] != 0:
        cases[parents[i]].append(i)

dfs(root, 1)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[a] != depth[b]:
        b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]
    print(a)
