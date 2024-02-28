import sys

input = sys.stdin.readline

n = int(input())
li = []
li = [int(input()) for _ in range(n)]
li.sort()

flag_li = []
for a in li[:10]: 
    for b in li[:10]:
        if a != b:
            flag_li.append(int(str(a)+str(b))) 
flag_li.sort() 
print(flag_li[2]) 
