from bisect import bisect_left

n = int(input())
li = list(map(int, input().split()))

cnt_li = [0]*n
tmp_li = [-10000000001]

for i in range(n):
	if li[i] > tmp_li[-1]:
		tmp_li.append(li[i])
		cnt_li[i] = len(tmp_li)
	else:
		tmp = bisect_left(tmp_li, li[i])
		tmp_li[tmp] = li[i]
		cnt_li[i] = tmp + 1

cnt = len(tmp_li)
flag_li = [0] * cnt

print(cnt-1)

for i in range(len(li) - 1, -1, -1):
    if cnt_li[i] == cnt:
        cnt-=1
        flag_li[cnt] = li[i]

del flag_li[0]
print(' '.join(map(str, flag_li)))