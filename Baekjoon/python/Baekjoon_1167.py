import sys

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    node = list(map(int, input().split()))
    for i in range(1, len(node)-1, 2):
        tree[node[0]].append((node[i], node[i+1]))

def dfs(start, tree):
    visited = [False] * (n+1)
    stack = [(start, 0)]
    visited[start] = True
    max_dist = [0, 0]
    while stack:
        node, dist = stack.pop()
        if dist > max_dist[1]:
            max_dist = [node, dist]
        for v, d in tree[node]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, dist+d))
    return max_dist

print(dfs(dfs(1, tree)[0], tree)[1])
