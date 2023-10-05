'''
from itertools import combinations

l, c = map(int, input().split())
dict_alp = {}

li = sorted(list(input().split()))
flag_li = list(combinations(list(range(1,c+1)), l))

for i in range(c):
  dict_alp[i+1] = li[i]

for x in flag_li:
  a = dict_alp[x[0]]+dict_alp[x[1]]+dict_alp[x[2]]+dict_alp[x[3]] # 아 테스트 케이스 4개라서 나도모르게 실수를.
  cnt = 0

  for i in a:
    if i in "aeiou":
      cnt += 1
  if cnt >= 1 and (len(a) - cnt) >= 2:
    print(a)  
    '''
  
# 아 해설 보고 틀린거 깨달았다 ..

from itertools import combinations
 
l, c = map(int,input().split())
alp = sorted(input().split())
words = combinations(alp, l)
 
for word in words:
    cnt = 0
    for i in word:
        if i in "aeiou":
            cnt += 1
 
    if cnt >= 1 and l - cnt >= 2:
      print(''.join(word))
