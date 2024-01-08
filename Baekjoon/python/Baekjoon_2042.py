import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (n+1)

def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    update(i, nums[i-1])

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c-nums[b-1])
        nums[b-1] = c
    else: # 2
        print(interval_sum(b, c))

