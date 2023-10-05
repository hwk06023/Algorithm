import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, d, x = map(int, input().split())
    last_v = a
    last_li = [0, a]
    
    j = 0
    while(last_v < x):
        last_v += last_v+d-last_li[j]
        last_li.append(last_v)
        j+=1

    print(j+1, x - last_li[j])
    
