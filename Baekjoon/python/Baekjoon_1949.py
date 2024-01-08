import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(cur):
    visited[cur] = 1
    for u in li[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0] 
            dp[cur][0] += max(dp[u][0], dp[u][1]) 

n = int(input())

cost = [0] + list(map(int, input().split()))
dp = [[0, cost[i]]*2 for i in range(n+1)]
visited = [0 for _ in range(n+1)]
li = [[] for _ in range(n+1)]

for _ in range(n-1):
    v, u = map(int, sys.stdin.readline().split())
    li[v].append(u)
    li[u].append(v)

dfs(1)
print(max(dp[1][1], dp[1][0]))