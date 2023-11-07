n, p, q = map(int, input().split())

dp = {}
dp[0] = 1

def solve(n):
    if n in dp:
        return dp[n]
    dp[n] = solve(n//p) + solve(n//q)
    return dp[n]

print(solve(n))
