import sys

input = sys.stdin.readline

n = int(input())

dic = {}
k, flag = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        flag += (n-1) - k
        k += 1
    elif x == 0:
        if 'x' in dic:
            dic['x'] += 1
        else:
            dic['x'] = 1
        if 'y' in dic:
            flag += dic['y']    
    elif y == 0:
        if 'y' in dic:
            dic['y'] += 1
        else:
            dic['y'] = 1

        if 'x' in dic:
            flag += dic['x']
    else:
        if y/x in dic:
            dic[y/x] += 1
        else:
            dic[y/x] = 1

        if (x/y)*(-1) in dic:
            flag += dic[(x/y)*(-1)]

print(flag)
