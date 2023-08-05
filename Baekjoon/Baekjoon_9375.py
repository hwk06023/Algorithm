import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    dic = {}
    m = int(input())
    if m == 0:
        print(0)
    else:
        for _ in range(m):
            a, b = input().split()

            if b in dic.keys():
                dic[b] += 1
            else:
                dic[b] = 1

        li = list(dic.values())
        flag = li[0] + 1
        for i in range(1, len(dic)):
            flag *= li[i]+1

        print(flag-1)
    
