import sys, math

input = sys.stdin.readline

n, m  = map(int, input().split())

dic = {}
for i in range(n):
    w, v = map(int, input().split())
    if v/w in dic:
        dic[v/w][0] += w
        dic[v/w][1] += v
    else:
        dic[v/w] = [w, v]

li = sorted(dic.items(), reverse = True)

a = 0
b = 1
for i in range(len(li)):
    if m >= li[i][1][0]:
        m -= li[i][1][0]
        a += li[i][1][1]
    else:
        b = li[i][1][0]
        a *= b
        a += li[i][1][1] * m
        break

k = math.gcd(a,b)
print(str(a//k)+"/"+str(b//k))