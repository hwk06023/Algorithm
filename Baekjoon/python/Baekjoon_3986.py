'''import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
    good_word = list(input().rstrip())
    tmp_cnt = len(good_word)
    index = tmp_cnt
    while tmp_cnt > 0:
        if good_word[tmp_cnt-1] == good_word[tmp_cnt-2]:
            del good_word[tmp_cnt-1]
            del good_word[tmp_cnt-2]
            index -= 2
            tmp_cnt = index
        tmp_cnt -= 1
    if not index:
        cnt += 1

print(cnt)'''

import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
    stack = []
    good_word = list(input().rstrip())

    for i in good_word:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        cnt += 1

print(cnt)