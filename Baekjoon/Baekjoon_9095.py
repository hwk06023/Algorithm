n = int(input())

dp = [0]
dp.insert(1, 1)
dp.insert(2, 2)
dp.insert(3, 4)

for i in range(0, n):
    x = int(input())
    for j in range(4, x + 1):
        dp.insert(j, dp[j - 3] + dp[j - 2] + dp[j - 1])
    print(dp[x])