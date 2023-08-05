import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = set()
for i in range(n):
    li.add(int(input()))

li = sorted(li)

cnt = 0
flag_li = [[]]*(n+1)

for i in range(len(li)-1, 0, -1):
    print(li[i])
    a = k // li[i]
    b = k % li[i]

    tmp_li = [k, b]
    if a > 0:
        for j in range(1, a):
            tmp_li.append(k - li[i]*j)

    for x in flag_li[i+1]:
        a = x // li[i]
        b = x % li[i]

        if a > 0:
            for j in range(1, a):
                tmp_li.append(x - li[i]*j)

    flag_li[i] = tmp_li

    print(k, a, b, tmp_li)
    print(flag_li)
