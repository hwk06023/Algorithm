num = int(input())

flag = []

for i in range(num):
    flag.append([])
    flag[i].append(int(input()))
    tmp = int(input())
    flag[i].append(tmp - 1)

map_li = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

for i in range(15):
    map_li.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for j in range(1, 14):
        map_li[i+1][j] = map_li[i][j] + map_li[i+1][j-1]

for i in range(num):
    print(map_li[flag[i][0]][flag[i][1]])
