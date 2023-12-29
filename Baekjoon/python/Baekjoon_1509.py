import sys

input = sys.stdin.readline

str_li = input.split()
str_len = len(str_li)

dp = [[0] * str_len for _ in range(str_len)]

for i in range(str_len):
    dp[i][i] = 1
    for j in range(i + 1, str_len):
        if str_li[i] == str_li[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

print(dp[0][str_len - 1])