n = int(input())

alp = []
alp_dict = {}
flag_li = []

for _ in range(n):
    alp.append(list(input()))

for i in range(n):
    for j in range(len(alp[i])):
        if alp[i][j] in alp_dict: 
            alp_dict[alp[i][j]] += 10 ** (len(alp[i])-j-1)
        else:
            alp_dict[alp[i][j]] = 10 ** (len(alp[i])-j-1)

for x in alp_dict.values():
    flag_li.append(x)

flag_li.sort(reverse=True)

flag = 0
t = 0
for x in flag_li:
    flag += x * (9 - t)
    t += 1

print(flag)