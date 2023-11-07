import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(input().rstrip()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        map[i][j] = int(map[i][j])
        if map[i][j] == 1:
            dp[i][j] = 1

for i in range(1, n):
    for j in range(1, m):
        if map[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            

flag = 0
for i in range(n):
    for j in range(m):
        if flag < dp[i][j]**2:
            flag = dp[i][j]**2

print(flag)