import sys

input = sys.stdin.readline
n = int(input())

boolean_li = [True] * 4000001
m = int(n ** 0.5)
for i in range(2, m + 1):
    if boolean_li[i] == True:
        for j in range(i*2, n+1, i):
            boolean_li[j] = False

prime_li = [i for i in range(2, n+1) if boolean_li[i] == True]

cnt = 0
start, end = 0, 0

if n == 1:
    print(0)
else:
    while end <= len(prime_li):
        temp_sum = sum(prime_li[start:end])
        if temp_sum == n:
            cnt += 1
            end += 1
        elif temp_sum < n:
            end += 1
        else:
            start += 1

    print(cnt)