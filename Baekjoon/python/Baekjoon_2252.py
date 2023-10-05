from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    w, v = map(int, input().split())
    graph[w].append(v)
    indegree[v] += 1

flag_li = []
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
while(q):
    tmp = q.popleft()
    flag_li.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
    

print(" ".join(map(str, flag_li)))

