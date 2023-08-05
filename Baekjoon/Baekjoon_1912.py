n = int(input())
li = list(map(int, input().split()))

flag_li = [li[0]]

for i in range(1, n):
    flag_li.append(max(li[i], flag_li[-1]+li[i]))

print(max(flag_li))