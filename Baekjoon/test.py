n, k = map(int, input().split())
li = []
cnt = 0
i_cnt = 0

for i in range(n):
    tmp_n = int(input())
    
    if tmp_n <= k:
        li.append(tmp_n)
    
li.sort(reverse=True)

for x in li:
    if k >= x:
        cnt += k // x
        k %= x
    
print(cnt)