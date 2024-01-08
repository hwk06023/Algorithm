k, n = map(int, input().split())

n -= 1

ans = [[1 if i == j else 0 for j in range(k + 2)] for i in range(k + 2)]
arr = [[1 if j <= i else 0 for j in range(k + 2)] for i in range(k + 2)]

while n > 0:
    if n % 2 == 1:
        result = [[0] * (k + 2) for _ in range(k + 2)]
        for i in range(k + 2):
            for j in range(k + 2):
                result[i][j] = sum(ans[i][a] * arr[a][j] for a in range(k + 2)) % 1000000007
        ans = result

    result = [[0] * (k + 2) for _ in range(k + 2)]
    for i in range(k + 2):
        for j in range(k + 2):
            result[i][j] = sum(arr[i][a] * arr[a][j] for a in range(k + 2)) % 1000000007
    arr = result

    n //= 2

print(sum(ans[k + 1]) % 1000000007)
