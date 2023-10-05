import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if (k == 1):
    print(1)
else:
    n += 1
    li = [[]] * k

    for i in range(k):
        li[i] = [1] * n

    for i in range(1, k):
        for j in range(1, n):
            li[i][j] = li[i-1][j] + li[i][j-1]

    print(li[k-1][n-1] % 1000000000)
