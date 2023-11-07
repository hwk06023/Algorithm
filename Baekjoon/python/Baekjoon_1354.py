n, p, q, x, y = map(int, input().split())

dp = {}
dp[0] = 1

def solve(n):
    if n in dp:
        return dp[n]
    tmp_x = (n//p)-x
    tmp_y = (n//q)-y

    if tmp_x < 0:
        tmp_x = 0
    if tmp_y < 0:
        tmp_y = 0

    dp[n] = solve(tmp_x) + solve(tmp_y)
    return dp[n]

print(solve(n))