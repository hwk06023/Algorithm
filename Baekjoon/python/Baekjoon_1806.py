import sys

input = sys.stdin.readline

n, s= map(int, input().split())
li = list(map(int, input().split()))

li_len = len(li)+1
start = 0
end = 0
tmp = li[0]

while start <= end:
    if tmp >= s:
        li_len = min(li_len, end - start + 1)
        tmp -= li[start]
        start += 1
    else:
        end += 1
        if end < n:
            tmp += li[end]
        else:
            break

print(0 if li_len == len(li)+1 else li_len)