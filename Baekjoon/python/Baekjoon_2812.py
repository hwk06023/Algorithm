import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().rstrip()))

stack = []
for i in range(n):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])

while k > 0:
    stack.pop()
    k -= 1

print(''.join(map(str, stack[:n - k])))