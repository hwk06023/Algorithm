import sys
input = sys.stdin.readline

n, k = map(int, input().split())

w, v = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(k+1):
    if i >= w:
        dp[0][i] = v

for i in range(1, n):
    w, v = map(int, input().split())
    for j in range(k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][k])