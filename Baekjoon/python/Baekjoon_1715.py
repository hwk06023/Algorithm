import sys

input = sys.stdin.readline

n = int(input())

li = [0] * (n)
li[0] = int(input())

if n == 1:
    print(li[0])
else:
    for i in range(1, n):
        li[i] = int(input())
    li.sort()
    print(li)
    while(1):
        li.append(li[0] + li[1])
        del li[0]
        del li[0]
        if len(li) == 1:
            break
        li.sort()
        print(li)
        
print(li[0]*2)