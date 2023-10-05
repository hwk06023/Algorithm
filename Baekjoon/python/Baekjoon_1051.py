n, m = map(int, input().split())

li = []
for i in range(n):
    li.append(list(input()))

tmp = 1
for i in range(n-1):
    for j in range(m-1):
        if li[i][j] in li[i][j+1:]:
            for k in range(j+1, m):
                if li[i][j] == li[i][k]:
                    if i + (k-j) < n:
                        if li[i][j] == li[i + (k-j)][j] and li[i][j] == li[i + (k-j)][k]:
                            if tmp < (k-j) + 1:
                                tmp = (k-j) + 1
                    
print(tmp ** 2)