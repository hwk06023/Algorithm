n = int(input())
li = list(map(int, input().split()))
r_li = li[::-1]

incre_li = [1] * n
decre_li = [1] * n

for i in range(1, n):
    tmp = -1
    k = -1
    bol = 0
    for j in range(i):
        if li[j] < li[i]:
            if incre_li[j] > tmp:
                tmp = incre_li[j]
                k = j
                bol = 1
        if r_li[j] < r_li[i]:
            decre_li[i] = max(decre_li[i], decre_li[j] + 1)
        if bol == 1:
            incre_li[i] = incre_li[k]+1
        else:
            incre_li[i] = 1

flag = 1
for i in range(n):
    tmp = incre_li[i] + decre_li[n-i-1]
    if flag < tmp:
        flag = tmp

print(flag-1)