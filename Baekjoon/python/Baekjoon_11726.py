x = int(input())

dp = [0]
dp.insert(1, 1)
dp.insert(2, 2)

for i in range(3, x+1):
    dp.insert(i, ((dp[i - 1] + dp[i - 2]) % 10007))

print(dp[x])