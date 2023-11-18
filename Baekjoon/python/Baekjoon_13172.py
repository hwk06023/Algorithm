import sys

input = sys.stdin.readline

m = int(input())
answer = 0
for _ in range(m):
    n, s = map(int, input().split())
    answer += (s * pow(n, -1, 1000000007)) % 1000000007
print(answer % 1000000007)
