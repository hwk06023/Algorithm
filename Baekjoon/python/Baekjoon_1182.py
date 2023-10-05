from itertools import product

n, s = map(int, input().split())

li = list(map(int, input().split()))

b_li = list(product([1, 0], repeat=n))
cnt = 0

for x in b_li:
    if sum(x) > 0:
        flag = 0
        for i in range(n):
            flag += li[i]*x[i]
        
        if flag == s:
            cnt += 1

print(cnt)