n = int(input())

li = [[' '] * ((2*n)-1) for _ in range(n)]

def star(n, x, y):
    if n == 3:
        li[x][y] = '*'
        li[x+1][y-1] = '*'
        li[x+1][y+1] = '*'
        for i in range(5):
            li[x+2][y-2+i] = '*'
    else:
        star((n//2), x, y)
        star((n//2), x+n//2, y-n//2)
        star((n//2), x+n//2, y+n//2)

star(n, 0, n-1)

for i in range(n):
    print(''.join(li[i]))
