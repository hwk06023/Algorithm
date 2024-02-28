import sys

input = sys.stdin.readline

n = int(input())
li_1 = []
li_2 = []
for _ in range(n):
    li_1.append(list(input().rstrip()))

for _ in range(n):
    li_2.append(list(map(int, input().split())))


