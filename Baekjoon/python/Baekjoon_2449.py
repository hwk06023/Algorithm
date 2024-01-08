import sys

input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())
bright = list(map(int, input().split()))
dp = [[-1] * 201 for _ in range(201)]

def solve(start, end):
    global bright, dp
    if start == end:
        return 0
    ret = dp[start][end]
    if ret != -1:
        return ret
    ret = INF

    for i in range(start, end):
        temp = 0 if bright[start] == bright[i + 1] else 1
        ret = min(ret, solve(start, i) + solve(i + 1, end) + temp)

    dp[start][end] = ret
    return ret

result = solve(0, n - 1)
print(result)

