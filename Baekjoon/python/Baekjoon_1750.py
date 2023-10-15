import sys
import math

input =  sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

dp = [0] * 1000001

for i in range(n):
    for j in range(1, 1000001):
        if dp[j]: dp[math.gcd(j, li[i])] += dp[j]
    dp[li[i]] += 1

print(dp[1] % 10000003)