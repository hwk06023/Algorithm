import sys

input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: (x[1], x[0]))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if graph[i][0] > graph[j][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
