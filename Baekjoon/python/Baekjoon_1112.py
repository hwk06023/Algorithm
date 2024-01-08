import sys

input = sys.stdin.readline

x, b = map(int, input().split())

if x == 0:
    print(0)
else:
    xb_bolean = b > 0 and x < 0
    if xb_bolean:
        x = -x
    
    li = []
    while x:
        q = x // b
        r = x % b
        if r < 0:
            q += 1
            r -= b
        li.append(r)
        x = q

    if xb_bolean:
        print('-', end='')
    
    print(''.join(map(str, li[::-1])))
