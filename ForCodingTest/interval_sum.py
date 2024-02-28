# 노노 투 포인터 누적 합
import sys

input = sys.stdin.readline

left, right = map(int, input().split())
li = list(map(int, input().split()))

sum_value = 0
sum_li = []

for x in li:
    sum_value = li[x]
    sum_li.append(sum_value)

print(sum_li[left] - sum_li[right])