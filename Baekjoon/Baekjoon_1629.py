import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

k = a%c
li = []

while b > 1:
    if b%2 == 1:
        li.append(1)
    else:
        li.append(0)
    b //= 2 

li = reversed(li)

for x in li:
    if x == 1:
        k = (((k**2) % c) * (a%c)) % c

    else:
        k = (k**2) % c

print(k)