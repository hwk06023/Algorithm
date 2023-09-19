n = int(input())

li = [[' '] * n for _ in range(n)]

def star(n, x, y):
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                li[x+i][y-j] = '*'
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(n//3, x+(n//3)*i, y-(n//3)*j)

star(n, 0, n-1)

for i in range(n):
    print(''.join(li[i]))