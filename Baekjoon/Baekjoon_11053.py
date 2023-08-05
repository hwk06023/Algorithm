n = int(input())
li = list(map(int, input().split()))

cnt_li = [1]*n

min_v = min(li)

for i in range(1, n):
	tmp = -1
	k = -1
	bol = 0
	for j in range(i):
		if li[j] < li[i]:
			if cnt_li[j] > tmp:
				tmp = cnt_li[j]
				k = j
				bol = 1
			
		if bol == 1:
			cnt_li[i] = cnt_li[k]+1
		else:
			cnt_li[i] = 1

print(cnt_li)
