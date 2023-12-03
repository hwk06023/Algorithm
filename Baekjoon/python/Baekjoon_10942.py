import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if li[i] == li[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if li[j] == li[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    print(dp[s][e])
