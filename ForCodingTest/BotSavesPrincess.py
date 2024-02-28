import sys

n = int(input())
map = []
bot = [0, 0]
princess = [0, 0]

for i in range(n):
    tmp = input()
    if 'm' in tmp:
        bot = [i, tmp.index('m')]
    elif 'p' in tmp:
        princess = [i, tmp.index('p')]
    map.append(list(tmp))
    
if bot[0] < princess[0]:
    for _ in range(princess[0]-bot[0]):
        print('DOWN')
elif bot[0] > princess[0]:
    for _ in range(bot[0]-princess[0]):
        print('UP')

if bot[1] < princess[1]:
    for _ in range(princess[1]-bot[1]):
        print('RIGHT')
elif bot[1] > princess[1]:
    for _ in range(bot[1]-princess[1]):
        print('LEFT')

