import sys

input = sys.stdin.readline

A, K = map(int, input().split())
li_a = list(map(int, input().split()))
tmp_li = [0]*K

def merge(li_a, tmp_li, left, mid, right):
    if left == right:
        return 0
    