n, c = map(int, input().split())

li = list(map(int, input().split()))
num_dict = {}

for i in range(n):
    if li[i] in num_dict:
        num_dict[li[i]][0] += 1
    else:
        num_dict[li[i]] = [1, i]

num_li = []

for key, value in num_dict.items():
    num_li.append([value[0], value[1], key])
num_li.sort(reverse=True, key=lambda x: (x[0], -x[1]))

for i in range(len(num_li)):
    for j in range(num_li[i][0]):
        print(num_li[i][2], end=' ')
print()
