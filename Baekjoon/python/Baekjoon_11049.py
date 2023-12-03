import sys

input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        dp[j][j+i] = float('inf')
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + graph[j][0] * graph[k][1] * graph[j+i][1])

print(dp[0][n-1])
