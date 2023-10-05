import sys, math

input = sys.stdin.readline

n = int(input())

if n*0.15 - math.floor(n*0.15) >= 0.5:
    r = math.ceil(n*0.15)
else:
    r = math.floor(n*0.15) 

if n == 0:
    print(0)

else:
    li = []
    for _ in range(n):
        li.append(int(input()))

    li.sort()
    li = li[r:n-r]

    if sum(li)/len(li) - math.floor(sum(li)/len(li)) >= 0.5:
        print(math.ceil(sum(li)/len(li)))
    else:
        print(math.floor(sum(li)/len(li)))
