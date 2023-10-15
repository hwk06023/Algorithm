n = int(input())

cnt = n
for _ in range(n):
    li = list(input())
    for i in range(len(li)):
        if li[i] in li[i+1:]:
            if li[i] != li[i+1]:
                cnt -= 1
                break

print(cnt)
