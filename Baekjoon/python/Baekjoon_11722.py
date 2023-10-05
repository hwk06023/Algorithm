n = int(input())
li = list(map(int, input().split()))

cnt_li = [1] * n

min_v = min(li)

for i in range(1, n):
	for j in range(i):
		if li[j] > li[i]:
			cnt_li[i] = max(cnt_li[i], cnt_li[j] + 1)

print(max(cnt_li))
