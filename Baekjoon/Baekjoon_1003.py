n = int(input())

dp = []
dp.insert(0, 1)
dp.insert(1, 1)

for i in range(2, n):
	dp.insert(i, dp[i-1] + dp[i-2])
	
print(dp[n-1])