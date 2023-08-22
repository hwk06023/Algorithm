import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    dist = y - x
    if dist == 1:
        print(1)
    else:
        for j in range(1, 800000):
            if (dist > j**2) and (dist <= (j+1) ** 2):
                if j+1 > ((j+1)**2)-dist:
                    print((j * 2) + 1)
                else:
                    print(j * 2)
                break